from odoo import models, fields, api, _
from odoo.exceptions import UserError
import json


class SelfAssessmentWizard(models.TransientModel):
    _name = 'competency.self.assessment.wizard'
    _description = 'Self-Assessment Wizard'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True,
        default=lambda self: self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1))
    discipline_id = fields.Many2one('competency.discipline', string='Discipline', required=True)
    assessment_date = fields.Date(default=fields.Date.today)
    line_ids = fields.One2many('competency.self.assessment.line.wizard', 'wizard_id',
        string='Competency Evaluations')

    def action_load_competencies(self):
        """Load all active competencies for the selected discipline into the wizard."""
        self.ensure_one()
        if not self.discipline_id:
            raise UserError(_('Please select a discipline first.'))
        # Clear existing lines
        self.line_ids.unlink()
        # Load active competencies
        competencies = self.env['competency.competency'].search([
            ('discipline_id', '=', self.discipline_id.id),
            ('active', '=', True),
        ], order='sequence, name')
        if not competencies:
            raise UserError(_('No active competencies found in this discipline.'))
        lines = []
        for comp in competencies:
            # Build criteria snapshot
            criteria_data = []
            for crit in comp.criterion_ids:
                criteria_data.append({
                    'level': crit.level_id.name,
                    'level_code': crit.level_id.code,
                    'description': crit.description,
                })
            criteria_json = json.dumps(criteria_data, indent=2) if criteria_data else '[]'
            lines.append((0, 0, {
                'competency_id': comp.id,
                'competency_name': comp.name,
                'competency_description': comp.description or '',
                'criteria_snapshot': criteria_json,
            }))
        self.write({'line_ids': lines})
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    def action_submit_assessment(self):
        """Submit the self-assessment: create the assessment record and snapshot."""
        self.ensure_one()
        if not self.env.user.has_group('competency_assessment.group_competency_admin'):
            if self.employee_id.user_id != self.env.user:
                from odoo.exceptions import AccessError
                raise AccessError(_('You can only submit assessments for yourself.'))
        if not self.line_ids:
            raise UserError(_('Please load competencies first.'))
        # Create the assessment
        assessment = self.env['competency.assessment'].create({
            'employee_id': self.employee_id.id,
            'discipline_id': self.discipline_id.id,
            'assessment_date': self.assessment_date,
        })
        # Create assessment lines (versioned snapshot)
        for line in self.line_ids:
            self.env['competency.assessment.line'].create({
                'assessment_id': assessment.id,
                'competency_id': line.competency_id.id,
                'competency_name': line.competency_name,
                'competency_description': line.competency_description,
                'criteria_snapshot': line.criteria_snapshot,
                'self_assessed_level_id': line.self_assessed_level_id.id,
                'employee_comment': line.employee_comment,
                'attachment_ids': [(6, 0, line.attachment_ids.ids)],
            })
        # Submit
        assessment.action_self_assess()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'competency.assessment',
            'res_id': assessment.id,
            'view_mode': 'form',
            'target': 'current',
        }


class SelfAssessmentLineWizard(models.TransientModel):
    _name = 'competency.self.assessment.line.wizard'
    _description = 'Self-Assessment Line'

    wizard_id = fields.Many2one('competency.self.assessment.wizard', required=True, ondelete='cascade')
    competency_id = fields.Many2one('competency.competency', readonly=True)
    competency_name = fields.Char(readonly=True)
    competency_description = fields.Text(readonly=True)
    criteria_snapshot = fields.Text(readonly=True)
    self_assessed_level_id = fields.Many2one('competency.level', string='Your Level')
    employee_comment = fields.Text(string='Comments')
    attachment_ids = fields.Many2many('ir.attachment', string='Evidence')
