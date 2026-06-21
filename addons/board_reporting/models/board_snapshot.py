from odoo import models, fields, api, _


class BoardSnapshot(models.Model):
    _name = 'board.snapshot'
    _description = 'KPI Snapshot'
    _order = 'snapshot_date desc, metric_id'
    _rec_name = 'snapshot_label'

    # ---- Identity ----
    metric_id = fields.Many2one(
        'board.metric', string='Metric',
        required=True, ondelete='cascade', index=True,
    )
    report_id = fields.Many2one(
        'board.report', string='Source Report',
        ondelete='set null', index=True,
        help='The board report that generated this snapshot.',
    )
    snapshot_date = fields.Datetime(
        string='Snapshot Date',
        default=fields.Datetime.now,
        required=True, index=True,
    )
    snapshot_label = fields.Char(
        string='Label',
        compute='_compute_label', store=True,
        help='Human-readable label, e.g. "Q2 2026 — Headcount".',
    )

    # ---- Data ----
    value = fields.Float(string='Value', required=True)
    period_start = fields.Date(string='Period Start')
    period_end = fields.Date(string='Period End')
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.company,
        required=True,
    )

    # ---- Display ----
    formatted_value = fields.Char(
        string='Formatted Value',
        compute='_compute_formatted_value', store=True,
    )
    metric_type = fields.Selection(
        related='metric_id.metric_type', store=True,
    )
    metric_category = fields.Selection(
        related='metric_id.category', store=True,
    )

    @api.depends('metric_id.name', 'period_start', 'period_end')
    def _compute_label(self):
        for rec in self:
            parts = []
            if rec.period_start:
                year = rec.period_start.year
                quarter = (rec.period_start.month - 1) // 3 + 1
                parts.append(f'Q{quarter} {year}')
            elif rec.period_end:
                year = rec.period_end.year
                quarter = (rec.period_end.month - 1) // 3 + 1
                parts.append(f'Q{quarter} {year}')
            if rec.metric_id:
                parts.append(rec.metric_id.name)
            rec.snapshot_label = ' — '.join(parts) if parts else 'Snapshot'

    @api.depends('value', 'metric_type')
    def _compute_formatted_value(self):
        for rec in self:
            val = rec.value
            mtype = rec.metric_type
            if mtype == 'percentage':
                rec.formatted_value = f'{val:.1f}%'
            elif mtype == 'count':
                rec.formatted_value = f'{int(val)}'
            elif mtype == 'currency':
                rec.formatted_value = f'£{val:,.2f}'
            elif mtype == 'hours':
                rec.formatted_value = f'{val:.1f}h'
            elif mtype == 'ratio':
                rec.formatted_value = f'{val:.2f}'
            else:
                rec.formatted_value = f'{val:.2f}'
