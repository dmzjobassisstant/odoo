from odoo import models, fields, api


class TrainingAssignment(models.Model):
    _name = 'training.assignment'
    _description = 'Training Assignment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'assigned_date desc'

    employee_id = fields.Many2one(
        'hr.employee', string='Employee',
        required=True, tracking=True,
    )
    course_id = fields.Many2one(
        'training.course', string='Course',
        required=True, tracking=True,
    )
    plan_id = fields.Many2one(
        'training.plan', string='Training Plan',
        related='course_id.plan_id', store=True,
    )
    assigned_by = fields.Many2one('hr.employee', string='Assigned By')
    assigned_date = fields.Date(
        string='Assigned Date',
        default=fields.Date.today,
    )
    due_date = fields.Date(string='Due Date')
    state = fields.Selection(
        [('assigned', 'Assigned'),
         ('in_progress', 'In Progress'),
         ('completed', 'Completed'),
         ('expired', 'Expired')],
        string='Status',
        default='assigned',
        tracking=True,
    )
    progress_pct = fields.Float(
        string='Progress (%)',
        default=0.0,
    )
    score = fields.Float(string='Score')
    completed_date = fields.Date(string='Completed Date')
    scorm_data = fields.Text(string='SCORM Data')
    notes = fields.Text(string='Notes')

    def action_start(self):
        self.ensure_one()
        self.state = 'in_progress'
        return True

    def action_complete(self):
        self.ensure_one()
        if self.state == 'completed':
            return True  # Already completed — prevent duplicate completion records
        self.state = 'completed'
        self.progress_pct = 100.0
        self.completed_date = fields.Date.today()
        # Create completion record
        self.env['training.completion'].create({
            'assignment_id': self.id,
            'employee_id': self.employee_id.id,
            'course_id': self.course_id.id,
            'completed_date': self.completed_date,
            'score': self.score,
        })
        return True

    def action_expire(self):
        self.state = 'expired'
        return True

    def action_launch_scorm(self):
        """Return the URL to launch the SCORM course."""
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return {
            'type': 'ir.actions.act_url',
            'url': f'/training/scorm/{self.id}',
            'target': 'new',
        }

    def _cron_expire_assignments(self):
        """Cron job to auto-expire assignments past due date."""
        today = fields.Date.today()
        expired = self.search([
            ('state', 'in', ['assigned', 'in_progress']),
            ('due_date', '<', today),
        ])
        expired.action_expire()
        return True
