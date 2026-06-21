from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date, timedelta


class HRPayslip(models.Model):
    _name = 'hr.payslip'
    _description = 'Payslip'
    _order = 'period_start desc, employee_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # ---- Basic Fields ----
    name = fields.Char(string='Reference', readonly=True, copy=False,
                       default='New', tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Employee',
                                   required=True, tracking=True, index=True)
    contract_id = fields.Many2one('hr.lifecycle.contract', string='Contract',
                                   tracking=True,
                                   domain="[('employee_id', '=', employee_id), ('state', '=', 'active')]")
    period_start = fields.Date(string='Period Start', required=True, tracking=True)
    period_end = fields.Date(string='Period End', required=True, tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
    ], string='Status', default='draft', tracking=True,
       group_expand='_group_expand_states')

    # ---- Financial Fields ----
    gross_pay = fields.Float(string='Gross Pay', compute='_compute_gross_pay',
                              store=True, tracking=True)
    ni_deduction = fields.Float(string='NI Deduction', tracking=True)
    tax_deduction = fields.Float(string='Income Tax', tracking=True)
    pension_deduction = fields.Float(string='Pension', tracking=True)
    other_deductions = fields.Float(string='Other Deductions', tracking=True)
    total_deductions = fields.Float(string='Total Deductions',
                                     compute='_compute_total_deductions',
                                     store=True, tracking=True)
    net_pay = fields.Float(string='Net Pay', compute='_compute_net_pay',
                            store=True, tracking=True)

    # ---- Related Data ----
    timesheet_ids = fields.Many2many('timesheet.week', string='Timesheets',
                                      readonly=True, tracking=True)
    payslip_line_ids = fields.One2many('hr.payslip.line', 'payslip_id',
                                        string='Payslip Lines', copy=True)
    company_id = fields.Many2one('res.company', string='Company',
                                  default=lambda self: self.env.company,
                                  required=True)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                   related='company_id.currency_id')

    # ---- Computed Fields ----
    @api.depends('payslip_line_ids.amount', 'payslip_line_ids.category')
    def _compute_gross_pay(self):
        for rec in self:
            rec.gross_pay = sum(
                line.amount for line in rec.payslip_line_ids
                if line.category == 'earning'
            )

    @api.depends('payslip_line_ids.amount', 'payslip_line_ids.category',
                 'ni_deduction', 'tax_deduction', 'pension_deduction',
                 'other_deductions')
    def _compute_total_deductions(self):
        for rec in self:
            line_deductions = sum(
                line.amount for line in rec.payslip_line_ids
                if line.category == 'deduction'
            )
            # Also include the legacy deduction fields if populated
            rec.total_deductions = (
                line_deductions +
                rec.ni_deduction +
                rec.tax_deduction +
                rec.pension_deduction +
                rec.other_deductions
            )

    @api.depends('gross_pay', 'total_deductions')
    def _compute_net_pay(self):
        for rec in self:
            rec.net_pay = rec.gross_pay - rec.total_deductions

    @api.depends('employee_id')
    def _compute_display_name(self):
        for rec in self:
            if rec.name and rec.name != 'New':
                rec.display_name = rec.name
            elif rec.employee_id:
                rec.display_name = _('Payslip - %(employee)s') % {
                    'employee': rec.employee_id.name
                }
            else:
                rec.display_name = _('New Payslip')

    def _group_expand_states(self, states, domain, order):
        return [key for key, _ in self._fields['state'].selection]

    # ---- Name Generation ----
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self._generate_name(vals)
        records = super().create(vals_list)
        for rec in records:
            if rec.name == 'New':
                rec.name = rec._generate_name({})
        return records

    def write(self, vals):
        result = super().write(vals)
        for rec in self:
            if rec.name == 'New' and rec.employee_id:
                rec.name = rec._generate_name({
                    'employee_id': rec.employee_id.id,
                    'period_start': rec.period_start,
                    'period_end': rec.period_end,
                })
        return result

    def _generate_name(self, vals):
        employee_id = vals.get('employee_id') or (
            self.employee_id.id if self.employee_id else None
        )
        period_start = vals.get('period_start') or self.period_start
        if not period_start:
            return 'New'

        if employee_id:
            employee = self.env['hr.employee'].browse(employee_id)
            emp_name = employee.name
        else:
            emp_name = 'Unknown'

        if isinstance(period_start, str):
            period_start = date.fromisoformat(period_start)

        month_name = period_start.strftime('%B %Y')
        return _('%(employee)s - %(month)s Payslip') % {
            'employee': emp_name,
            'month': month_name,
        }

    # ---- Onchange ----
    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        if self.employee_id:
            active_contract = self.env['hr.lifecycle.contract'].search([
                ('employee_id', '=', self.employee_id.id),
                ('state', '=', 'active'),
            ], limit=1)
            self.contract_id = active_contract.id if active_contract else False

    # ---- Generate Payslip ----
    def action_generate_lines(self):
        """Generate payslip lines from timesheet data and salary rules."""
        self.ensure_one()
        if self.state != 'draft':
            raise UserError(_('Can only generate lines for draft payslips.'))

        # Clear existing lines
        self.payslip_line_ids.unlink()

        # Pull submitted timesheets in the period for this employee
        timesheets = self.env['timesheet.week'].search([
            ('employee_id', '=', self.employee_id.id),
            ('state', 'in', ('submitted', 'completed')),
            ('week_start', '>=', self.period_start),
            ('week_end', '<=', self.period_end),
        ])
        self.timesheet_ids = timesheets

        # Get active contract
        if not self.contract_id:
            self.contract_id = self.env['hr.lifecycle.contract'].search([
                ('employee_id', '=', self.employee_id.id),
                ('state', '=', 'active'),
            ], limit=1)

        # Calculate gross pay from timesheets
        total_hours = sum(ts.total_hours for ts in timesheets)
        hourly_rate = self._get_hourly_rate()

        # Determine gross from hours × rate or contract salary
        if total_hours > 0 and hourly_rate > 0:
            gross_pay = total_hours * hourly_rate
        elif self.contract_id:
            gross_pay = self.contract_id.wage
        else:
            gross_pay = 0.0

        line_seq = 10

        # Create earning lines
        if total_hours > 0 and hourly_rate > 0:
            self.env['hr.payslip.line'].create({
                'payslip_id': self.id,
                'name': _('Basic Pay (%(hours).2f hours × £%(rate).2f/hr)') % {
                    'hours': total_hours,
                    'rate': hourly_rate,
                },
                'category': 'earning',
                'amount': gross_pay,
                'sequence': line_seq,
            })
            line_seq += 10

            # Overtime (hours > standard ~160/month for full-time)
            standard_hours = 160.0
            if total_hours > standard_hours:
                overtime_hours = total_hours - standard_hours
                overtime_pay = overtime_hours * hourly_rate * 1.5
                self.env['hr.payslip.line'].create({
                    'payslip_id': self.id,
                    'name': _('Overtime (%(hours).2f hours × £%(rate).2f/hr)') % {
                        'hours': overtime_hours,
                        'rate': hourly_rate * 1.5,
                    },
                    'category': 'earning',
                    'amount': overtime_pay,
                    'sequence': line_seq,
                })
                gross_pay += overtime_pay
                line_seq += 10
        elif self.contract_id and self.contract_id.wage > 0:
            # Use contract wage as monthly salary
            self.env['hr.payslip.line'].create({
                'payslip_id': self.id,
                'name': _('Monthly Salary'),
                'category': 'earning',
                'amount': self.contract_id.wage,
                'sequence': line_seq,
            })
            line_seq += 10

        # Apply auto salary rules
        rules = self.env['hr.salary.rule'].search([
            ('applies_to_all', '=', True),
            ('active', '=', True),
        ], order='category, sequence')

        for rule in rules:
            if rule.category == 'earning':
                if rule.rate_type == 'percentage':
                    amount = gross_pay * (rule.rate_value / 100.0)
                else:
                    amount = rule.rate_value
                if amount > 0:
                    self.env['hr.payslip.line'].create({
                        'payslip_id': self.id,
                        'name': rule.name,
                        'category': 'earning',
                        'amount': amount,
                        'sequence': line_seq,
                    })
                    line_seq += 10

        # Deductions from rules
        total_earnings_for_deductions = sum(
            line.amount for line in self.payslip_line_ids
            if line.category == 'earning'
        )

        for rule in rules:
            if rule.category == 'deduction':
                if rule.rate_type == 'percentage':
                    amount = total_earnings_for_deductions * (rule.rate_value / 100.0)
                else:
                    amount = rule.rate_value
                if amount > 0:
                    self.env['hr.payslip.line'].create({
                        'payslip_id': self.id,
                        'name': rule.name,
                        'category': 'deduction',
                        'amount': amount,
                        'sequence': line_seq,
                    })
                    line_seq += 10

        return True

    def _get_hourly_rate(self):
        """Derive hourly rate from contract."""
        self.ensure_one()
        if not self.contract_id:
            return 0.0

        wage = self.contract_id.wage
        contract_type = self.contract_id.contract_type

        if contract_type in ('permanent', 'fixed_term'):
            # Assume annual salary, convert to hourly
            # Standard: 52 weeks × 40 hours = 2080 hours/year
            return wage / (52 * 40) if wage > 0 else 0.0
        elif contract_type in ('contractor', 'zero_hours'):
            # Assume hourly rate directly
            return wage
        else:
            return 0.0

    # ---- Workflow Actions ----
    def action_confirm(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError(_('Payslip "%s" must be in Draft state to confirm.') % rec.name)
            if not rec.payslip_line_ids:
                raise UserError(_('Payslip "%s" has no lines. Please generate lines first.') % rec.name)
            rec.state = 'confirmed'
            rec.message_post(body=_('Payslip confirmed by %s.') % self.env.user.name)
        return True

    def action_mark_paid(self):
        for rec in self:
            if rec.state != 'confirmed':
                raise UserError(_('Payslip "%s" must be in Confirmed state to mark as paid.') % rec.name)
            rec.state = 'paid'
            rec.message_post(body=_('Payslip marked as paid by %s.') % self.env.user.name)
        return True

    def action_reset_draft(self):
        for rec in self:
            if rec.state == 'draft':
                continue
            rec.state = 'draft'
            rec.message_post(body=_('Payslip reset to draft by %s.') % self.env.user.name)
        return True

    def action_print_payslip(self):
        """Return the PDF report action — uses enhanced template when available."""
        self.ensure_one()
        # Try enhanced report from document_templates, fallback to original
        enhanced_ref = self.env.ref('document_templates.action_report_payslip_enhanced', raise_if_not_found=False)
        if enhanced_ref:
            return enhanced_ref.report_action(self)
        return self.env.ref('hr_payroll_custom.action_report_payslip').report_action(self)

    # ---- Constraints ----
    @api.constrains('period_start', 'period_end')
    def _check_period(self):
        for rec in self:
            if rec.period_start and rec.period_end and rec.period_end < rec.period_start:
                raise UserError(_('Period end date cannot be before period start date.'))

    @api.constrains('employee_id', 'period_start', 'period_end')
    def _check_duplicate_payslip(self):
        for rec in self:
            if rec.period_start and rec.period_end and rec.employee_id:
                duplicate = self.search([
                    ('employee_id', '=', rec.employee_id.id),
                    ('period_start', '=', rec.period_start),
                    ('period_end', '=', rec.period_end),
                    ('id', '!=', rec.id),
                ], limit=1)
                if duplicate:
                    raise UserError(_(
                        'A payslip already exists for %(employee)s for period %(start)s to %(end)s.'
                    ) % {
                        'employee': rec.employee_id.name,
                        'start': rec.period_start,
                        'end': rec.period_end,
                    })
