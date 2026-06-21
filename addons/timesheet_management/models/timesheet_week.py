from odoo import models, fields, api, _
from odoo.exceptions import UserError, AccessError
from datetime import timedelta


class TimesheetWeek(models.Model):
    _name = 'timesheet.week'
    _description = 'Timesheet Week'
    _order = 'week_start desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _default_employee(self):
        return self.env['hr.employee'].search(
            [('user_id', '=', self.env.uid)], limit=1
        )

    name = fields.Char(
        string='Reference',
        readonly=True,
        copy=False,
        default='New',
    )
    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        required=True,
        default=_default_employee,
        tracking=True,
        help='The employee this timesheet belongs to.',
    )
    user_id = fields.Many2one(
        'res.users',
        string='User',
        related='employee_id.user_id',
        store=True,
        readonly=True,
    )
    week_start = fields.Date(
        string='Week Start (Monday)',
        required=True,
        default=lambda self: self._default_week_start(),
        tracking=True,
    )
    week_end = fields.Date(
        string='Week End (Sunday)',
        compute='_compute_week_end',
        store=True,
        readonly=False,
        tracking=True,
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('completed', 'Completed'),
    ], string='Status', default='draft', tracking=True,
       group_expand='_group_expand_states')
    total_hours = fields.Float(
        string='Total Hours',
        compute='_compute_total_hours',
        store=True,
        tracking=True,
    )
    entry_ids = fields.One2many(
        'timesheet.entry',
        'week_id',
        string='Timesheet Entries',
        copy=True,
    )
    # Task list on this timesheet (computed from entries, for display)
    task_ids = fields.Many2many(
        'project.task',
        string='Tasks This Week',
        compute='_compute_task_ids',
        store=True,
    )
    submitted_date = fields.Datetime(
        string='Submitted On',
        readonly=True,
        tracking=True,
    )
    completed_date = fields.Datetime(
        string='Completed On',
        readonly=True,
        tracking=True,
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True,
    )

    # ---- Helpers ----

    @api.model
    def _default_week_start(self):
        today = fields.Date.today()
        return today - timedelta(days=today.weekday())

    @api.depends('week_start')
    def _compute_week_end(self):
        for rec in self:
            if rec.week_start:
                rec.week_end = rec.week_start + timedelta(days=6)

    @api.depends('entry_ids.hours')
    def _compute_total_hours(self):
        for rec in self:
            rec.total_hours = sum(entry.hours for entry in rec.entry_ids)

    @api.depends('entry_ids.task_id')
    def _compute_task_ids(self):
        for rec in self:
            rec.task_ids = rec.entry_ids.mapped('task_id')

    def _group_expand_states(self, states, domain, order):
        return [key for key, _ in self._fields['state'].selection]

    # ---- Name generation ----

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
        is_admin = self.env.user.has_group('timesheet_management.group_timesheet_admin')
        protected_fields = {'entry_ids', 'total_hours', 'week_start', 'week_end', 'employee_id'}
        admin_unlocking = is_admin and vals.get('state') == 'draft'

        for rec in self:
            if rec.state != 'draft' and not admin_unlocking:
                blocked = protected_fields & set(vals.keys())
                if blocked:
                    raise UserError(_(
                        'Timesheet "%(name)s" is in %(state)s state. '
                        'You cannot modify the following fields: %(fields)s. '
                        'Unlock the timesheet first.'
                    ) % {
                        'name': rec.name,
                        'state': dict(self._fields['state'].selection).get(rec.state, rec.state),
                        'fields': ', '.join(sorted(blocked)),
                    })

        return super().write(vals)

    def _generate_name(self, vals):
        week_start = vals.get('week_start') or self.week_start
        if not week_start:
            week_start = self._default_week_start()
        if isinstance(week_start, str):
            from datetime import date as dt_date
            week_start = dt_date.fromisoformat(week_start)

        iso_year, iso_week, _dow = week_start.isocalendar()
        week_end_date = week_start + timedelta(days=6)

        def fmt(d):
            return d.strftime('%m/%d')

        return _('Week %(week_num)s (Mon %(mon)s–Sun %(sun)s, %(year)s)') % {
            'week_num': iso_week,
            'mon': fmt(week_start),
            'sun': fmt(week_end_date),
            'year': week_start.year,
        }

    @api.onchange('week_start')
    def _onchange_week_start(self):
        if self.week_start and self.name in ('New', ''):
            self.name = self._generate_name({'week_start': self.week_start})

    # ---- Week day labels (for the UI header) ----

    def _get_week_days(self):
        """Return list of (day_name, date) tuples for this week."""
        self.ensure_one()
        if not self.week_start:
            return []
        DAY_NAMES = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        return [
            (DAY_NAMES[i], self.week_start + timedelta(days=i))
            for i in range(7)
        ]

    # ---- Add task to week (creates 7 day slots) ----

    def _add_task(self, task_id):
        """Create 7 entry slots (Mon-Sun) for a single task. Returns the created entries."""
        self.ensure_one()
        if not self.week_start:
            raise UserError(_('Please set the week start date first.'))
        task = self.env['project.task'].browse(task_id)
        if not task.exists():
            raise UserError(_('Task not found.'))

        DAY_NAMES = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        created = self.env['timesheet.entry']
        for day_offset in range(7):
            day_date = self.week_start + timedelta(days=day_offset)
            # Skip if entry already exists for this date+task
            existing = self.entry_ids.filtered(
                lambda e, d=day_date, t=task: e.date == d and e.task_id == t
            )
            if not existing:
                created += self.env['timesheet.entry'].create({
                    'week_id': self.id,
                    'date': day_date,
                    'task_id': task.id,
                    'day_name': DAY_NAMES[day_offset],
                    'hours': 0.0,
                    'description': '',
                })
        return created

    def _add_tasks(self, task_ids):
        """Create 7 day slots for each task in task_ids."""
        self.ensure_one()
        created = self.env['timesheet.entry']
        for tid in task_ids:
            created |= self._add_task(tid)
        return created

    # ---- Workflow Actions ----

    def action_submit(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError(_(
                    'Timesheet "%s" must be in Draft state to submit.'
                ) % rec.name)
            if not rec.entry_ids:
                raise UserError(_(
                    'Timesheet "%s" has no entries. Please add at least one task before submitting.'
                ) % rec.name)
            rec.write({
                'state': 'submitted',
                'submitted_date': fields.Datetime.now(),
            })
            rec.message_post(body=_('Timesheet submitted by %s.') % self.env.user.name)
        return True

    def action_unlock(self):
        if not self.env.user.has_group('timesheet_management.group_timesheet_admin'):
            raise AccessError(_('Only Timesheet Administrators can unlock timesheets.'))
        for rec in self:
            if rec.state not in ('submitted', 'completed'):
                raise UserError(_(
                    'Timesheet "%s" can only be unlocked from Submitted or Completed state.'
                ) % rec.name)
            rec.write({
                'state': 'draft',
                'submitted_date': False,
                'completed_date': False,
            })
            rec.message_post(body=_('Timesheet unlocked by %s.') % self.env.user.name)
        return True

    def action_complete(self):
        if not self.env.user.has_group('timesheet_management.group_timesheet_admin'):
            raise AccessError(_('Only Timesheet Administrators can mark timesheets as completed.'))
        for rec in self:
            if rec.state != 'submitted':
                raise UserError(_(
                    'Timesheet "%s" must be in Submitted state to mark as completed.'
                ) % rec.name)
            rec.write({
                'state': 'completed',
                'completed_date': fields.Datetime.now(),
            })
            rec.message_post(body=_('Timesheet marked as completed by %s.') % self.env.user.name)
        return True

    def action_return_to_submitted(self):
        if not self.env.user.has_group('timesheet_management.group_timesheet_admin'):
            raise AccessError(_('Only Timesheet Administrators can return timesheets to Submitted.'))
        for rec in self:
            if rec.state != 'completed':
                raise UserError(_(
                    'Timesheet "%s" must be in Completed state to return to Submitted.'
                ) % rec.name)
            rec.write({
                'state': 'submitted',
                'completed_date': False,
            })
            rec.message_post(body=_('Timesheet returned to Submitted by %s (billing dispute).')
                             % self.env.user.name)
        return True

    def action_reset_draft(self):
        if not self.env.user.has_group('timesheet_management.group_timesheet_admin'):
            raise AccessError(_('Only Timesheet Administrators can reset timesheets to draft.'))
        for rec in self:
            if rec.state == 'draft':
                continue
            rec.write({
                'state': 'draft',
                'submitted_date': False,
                'completed_date': False,
            })
            rec.message_post(body=_('Timesheet reset to draft by %s.') % self.env.user.name)
        return True

    # ---- Add Tasks action (opens wizard) ----

    def action_add_tasks(self):
        """Open the Add Tasks wizard to select tasks and create day slots."""
        self.ensure_one()
        if self.state != 'draft':
            raise UserError(_('You can only add tasks when the timesheet is in Draft state.'))
        return {
            'type': 'ir.actions.act_window',
            'name': _('Add Tasks to Week'),
            'res_model': 'timesheet.add.tasks.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_week_id': self.id,
                'default_employee_id': self.employee_id.id,
            },
        }

    # ---- Copy Tasks from Previous Week ----

    def action_copy_previous_week_tasks(self):
        """Copy task assignments from the previous week's timesheet.
        Does NOT copy hours or descriptions — just the task list."""
        self.ensure_one()
        if self.state != 'draft':
            raise UserError(_('You can only copy tasks when the timesheet is in Draft state.'))

        # Find the previous week's timesheet for the same employee
        prev_week_start = self.week_start - timedelta(days=7)
        prev_ts = self.search([
            ('employee_id', '=', self.employee_id.id),
            ('week_start', '=', prev_week_start),
        ], limit=1)

        if not prev_ts:
            raise UserError(_(
                'No timesheet found for %(name)s for the previous week (%(week)s). '
                'Create one first, or use "Add Tasks" to select tasks manually.'
            ) % {
                'name': self.employee_id.name,
                'week': prev_week_start.strftime('%m/%d/%Y'),
            })

        # Get distinct task IDs from previous week's entries
        prev_task_ids = prev_ts.entry_ids.mapped('task_id').ids
        if not prev_task_ids:
            raise UserError(_(
                'The previous week\'s timesheet has no tasks. '
                'Use "Add Tasks" to select tasks manually.'
            ))

        # Create 7-day slots for each task (skipping tasks already on this week)
        new_count = 0
        for tid in prev_task_ids:
            existing = self.entry_ids.filtered(lambda e, t=tid: e.task_id.id == t)
            if not existing:
                self._add_task(tid)
                new_count += 1

        if new_count == 0:
            raise UserError(_(
                'All tasks from the previous week are already on this timesheet.'
            ))
        self.message_post(body=_(
            'Copied %(count)s task(s) from previous week (%(week)s).'
        ) % {'count': new_count, 'week': prev_ts.name})
        return True
