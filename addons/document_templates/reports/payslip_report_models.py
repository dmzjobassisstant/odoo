from odoo import models, api


class ReportPayslipEnhanced(models.AbstractModel):
    _name = 'report.document_templates.report_payslip_enhanced'
    _description = 'Enhanced Payslip Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['hr.payslip'].browse(docids)

        template = self.env['document.template'].search([
            ('model', '=', 'hr.payslip'),
            ('template_type', '=', 'payslip'),
            ('is_default', '=', True),
            ('company_id', '=', self.env.company.id),
        ], limit=1)

        css_override = template.css_override or ''
        header_html = template.header_html or ''
        footer_html = template.footer_html or ''

        return {
            'doc_ids': docids,
            'doc_model': 'hr.payslip',
            'docs': docs,
            'css_override': css_override,
            'custom_header': header_html,
            'custom_footer': footer_html,
        }
