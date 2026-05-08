# Requirements: mrp_subcontracting

**Module:** MRP Subcontracting
**Version:** 0.1
**Category:** Supply Chain/Manufacturing
**Author:** Odoo S.A.
**License:** LGPL-3
**Website:** https://www.odoo.com/app/manufacturing

## Dependencies
- `mrp`

## Hooks
- `uninstall_hook` → `uninstall_hook`

## Models
- `mrp_bom`
- `mrp_production`
- `mrp_unbuild`
- `product`
- `res_company`
- `res_partner`
- `stock_location`
- `stock_move`
- `stock_move_line`
- `stock_picking`
- `stock_quant`
- `stock_rule`
- `stock_warehouse`

## Data Files
- `data/mrp_subcontracting_data.xml`
- `security/mrp_subcontracting_security.xml`
- `security/ir.model.access.csv`
- `views/mrp_bom_views.xml`
- `views/res_partner_views.xml`
- `views/stock_warehouse_views.xml`
- `views/stock_move_views.xml`
- `views/stock_quant_views.xml`
- `views/stock_picking_views.xml`
- `views/supplier_info_views.xml`
- `views/mrp_production_views.xml`
- `views/subcontracting_portal_views.xml`
- `views/subcontracting_portal_templates.xml`

## Demo Files
- `data/mrp_subcontracting_demo.xml`

## Security
- `ir.model.access.csv`
- `mrp_subcontracting_security.xml`

## Views
- `mrp_bom_views.xml`
- `mrp_production_views.xml`
- `res_partner_views.xml`
- `stock_move_views.xml`
- `stock_picking_views.xml`
- `stock_quant_views.xml`
- `stock_warehouse_views.xml`
- `subcontracting_portal_templates.xml`
- `subcontracting_portal_views.xml`
- `supplier_info_views.xml`

## Wizards
- `__init__.py`
- `change_production_qty.py`
- `mrp_production_serial_numbers.py`
- `stock_picking_return.py`

## Reports
- `__init__.py`
- `mrp_report_bom_structure.py`

## Asset Bundles
- `web.assets_tests` (1 entries)
- `web.assets_backend` (2 entries)
- `web.assets_frontend` (1 entries)
- `mrp_subcontracting.webclient` (84 entries)

## Install Settings
- **Installable:** `True`
- **Auto-install:** `False`
- **Application:** `False`
