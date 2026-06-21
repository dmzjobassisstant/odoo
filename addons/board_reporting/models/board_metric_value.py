from odoo import models, fields, api, _


class BoardMetricValue(models.Model):
    _name = 'board.metric.value'
    _description = 'Board Metric Value'
    _order = 'metric_id'

    report_id = fields.Many2one(
        'board.report',
        string='Report',
        required=True,
        ondelete='cascade',
    )
    metric_id = fields.Many2one(
        'board.metric',
        string='Metric',
        required=True,
        ondelete='restrict',
    )
    value = fields.Float(
        string='Value',
        required=True,
    )
    formatted_value = fields.Char(
        string='Formatted Value',
        compute='_compute_formatted_value',
        store=True,
    )
    trend = fields.Selection([
        ('up', 'Up'),
        ('down', 'Down'),
        ('stable', 'Stable'),
    ], string='Trend')
    previous_value = fields.Float(
        string='Previous Period Value',
    )
    notes = fields.Text(
        string='Notes',
    )

    @api.depends('value', 'metric_id.metric_type')
    def _compute_formatted_value(self):
        for rec in self:
            val = rec.value
            mtype = rec.metric_id.metric_type
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
