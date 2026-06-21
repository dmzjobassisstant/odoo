from odoo import models, api


class ReportInvoiceEnhanced(models.AbstractModel):
    _name = 'report.document_templates.report_invoice_enhanced'
    _description = 'Enhanced Invoice Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
        }
