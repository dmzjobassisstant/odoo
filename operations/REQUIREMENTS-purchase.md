# Requirements: purchase

**Module:** Purchase
**Version:** 1.2
**Category:** Supply Chain/Purchase
**Author:** Odoo S.A.
**License:** LGPL-3
**Website:** https://www.odoo.com/app/purchase

## Dependencies
- `account`

## Models
- `account_invoice`
- `account_tax`
- `analytic_account`
- `analytic_applicability`
- `ir_actions_report`
- `product`
- `purchase_bill_line_match`
- `purchase_order`
- `purchase_order_line`
- `res_company`
- `res_config_settings`
- `res_partner`

## Data Files
- `security/purchase_security.xml`
- `security/ir.model.access.csv`
- `data/digest_data.xml`
- `views/account_move_views.xml`
- `data/purchase_data.xml`
- `data/ir_cron_data.xml`
- `report/purchase_reports.xml`
- `views/purchase_views.xml`
- `views/purchase_bill_line_match_views.xml`
- `views/res_config_settings_views.xml`
- `views/product_views.xml`
- `views/res_partner_views.xml`
- `report/purchase_bill_views.xml`
- `report/purchase_report_views.xml`
- `data/mail_templates.xml`
- `data/mail_template_data.xml`
- `views/portal_templates.xml`
- `report/purchase_order_templates.xml`
- `report/purchase_quotation_templates.xml`
- `views/analytic_account_views.xml`
- `wizard/bill_to_po_wizard_views.xml`
- `data/purchase_tour.xml`

## Demo Files
- `data/purchase_demo.xml`

## Security
- `ir.model.access.csv`
- `purchase_security.xml`

## Views
- `account_move_views.xml`
- `analytic_account_views.xml`
- `portal_templates.xml`
- `product_views.xml`
- `purchase_bill_line_match_views.xml`
- `purchase_views.xml`
- `res_config_settings_views.xml`
- `res_partner_views.xml`

## Wizards
- `__init__.py`
- `bill_to_po_wizard.py`
- `bill_to_po_wizard_views.xml`

## Reports
- `__init__.py`
- `purchase_bill.py`
- `purchase_bill_views.xml`
- `purchase_order_templates.xml`
- `purchase_quotation_templates.xml`
- `purchase_report.py`
- `purchase_report_views.xml`
- `purchase_reports.xml`

## Asset Bundles
- `web.assets_backend` (8 entries)
- `web.assets_frontend` (2 entries)
- `web.assets_tests` (1 entries)

## Install Settings
- **Installable:** `True`
- **Auto-install:** `False`
- **Application:** `True`
