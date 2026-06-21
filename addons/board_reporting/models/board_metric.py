from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class BoardMetric(models.Model):
    _name = 'board.metric'
    _description = 'Board Metric'
    _order = 'sequence, name'

    name = fields.Char(
        string='Metric Name',
        required=True,
        translate=True,
    )
    code = fields.Char(
        string='Code',
        required=True,
        help='Unique identifier for this metric.',
    )
    description = fields.Text(
        string='Description',
        help='Detailed explanation of what this metric measures.',
    )
    category = fields.Selection([
        ('hr', 'HR'),
        ('finance', 'Finance'),
        ('operations', 'Operations'),
        ('sales', 'Sales'),
        ('project', 'Project'),
    ], string='Category', required=True, default='hr')
    metric_type = fields.Selection([
        ('percentage', 'Percentage'),
        ('count', 'Count'),
        ('currency', 'Currency'),
        ('hours', 'Hours'),
        ('ratio', 'Ratio'),
    ], string='Metric Type', required=True, default='count')
    calculation_method = fields.Text(
        string='Calculation Method',
        help='Method name (e.g. _compute_headcount) used to calculate this metric. '
             'For SQL-based metrics, store the SQL query here.',
    )
    target_value = fields.Float(
        string='Target Value',
        help='Target KPI value for this metric.',
    )
    is_active = fields.Boolean(
        string='Active',
        default=True,
        help='Only active metrics are calculated in reports.',
    )
    sequence = fields.Integer(
        string='Sequence',
        default=10,
    )
    snapshot_ids = fields.One2many(
        'board.snapshot', 'metric_id',
        string='Historical Snapshots',
    )

    _code_unique = models.Constraint(
        'UNIQUE(code)',
        'The metric code must be unique!',
    )

    def _run_calculation(self, report):
        """Execute the calculation method for this metric on the given report.
        Returns the computed float value.
        """
        self.ensure_one()
        method_name = (self.calculation_method or '').strip()
        if not method_name:
            raise UserError(_('Metric "%s" has no calculation method defined.') % self.name)
        # Security: whitelist allowed calculation methods
        allowed = {
            '_compute_timesheet_hours', '_compute_leave_days',
            '_compute_headcount', '_compute_revenue_per_employee',
            '_compute_absenteeism_rate', '_compute_turnover_rate',
            '_compute_avg_salary', '_compute_training_completion',
            '_compute_issue_resolution_time',
        }
        if method_name not in allowed:
            raise UserError(_('Unknown calculation method: %s') % method_name)
        result = getattr(report, method_name)(report.period_start, report.period_end)
        return result
