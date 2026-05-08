# Requirements: mrp_account

**Module:** Accounting - MRP
**Version:** 1.0
**Category:** Supply Chain/Manufacturing
**Author:** Odoo S.A.
**License:** LGPL-3
**Website:** https://www.odoo.com/app/manufacturing

## Description
Analytic Accounting in MRP
==========================

* Cost structure report

Also, allows to compute the cost of the product based on its BoM, using the costs of its components and work center operations.
It adds a button on the product itself but also an action in the list view of the products.
If the automated inventory valuation is active, the necessary accounting entries will be created.

## Dependencies
- `mrp`
- `stock_account`

## Hooks
- `post_init_hook` → `_configure_journals`

## Models
- `account_move`
- `analytic_account`
- `mrp_production`
- `mrp_workcenter`
- `mrp_workorder`
- `product`
- `stock_move`

## Data Files
- `security/ir.model.access.csv`
- `views/product_views.xml`
- `views/mrp_production_views.xml`
- `views/analytic_account_views.xml`
- `views/account_move_views.xml`
- `views/mrp_workcenter_views.xml`
- `report/report_mrp_templates.xml`
- `wizard/mrp_wip_accounting.xml`

## Demo Files
- `data/mrp_account_demo.xml`

## Security
- `ir.model.access.csv`

## Views
- `account_move_views.xml`
- `analytic_account_views.xml`
- `mrp_production_views.xml`
- `mrp_workcenter_views.xml`
- `product_views.xml`

## Wizards
- `__init__.py`
- `mrp_wip_accounting.py`
- `mrp_wip_accounting.xml`

## Reports
- `__init__.py`
- `mrp_report_mo_overview.py`
- `report_mrp_templates.xml`
- `stock_valuation_report.py`

## Asset Bundles
- `web.assets_backend` (1 entries)

## Install Settings
- **Installable:** `True`
- **Auto-install:** `True`
- **Application:** `False`
