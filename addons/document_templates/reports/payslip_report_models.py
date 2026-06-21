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

        font_map = {
            'helvetica': '"Helvetica Neue", Helvetica, Arial, sans-serif',
            'times': '"Times New Roman", Times, serif',
            'courier': '"Courier New", Courier, monospace',
        }
        font = font_map.get(template.font_family or 'helvetica', font_map['helvetica'])

        return {
            'doc_ids': docids,
            'doc_model': 'hr.payslip',
            'docs': docs,
            'logo': template.logo or False,
            'primary_color': template.primary_color or '#261e58',
            'secondary_color': template.secondary_color or '#f0eef7',
            'font_family': font,
            'css_override': template.css_override or '',
            'custom_header': template.header_html or '',
            'custom_footer': template.footer_html or '',
        }
