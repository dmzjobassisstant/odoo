# Requirements: purchase_requisition

**Module:** Purchase Agreements
**Version:** 0.1
**Category:** Supply Chain/Purchase
**Author:** Odoo S.A.
**License:** LGPL-3
**Website:** N/A

## Description
This module allows you to manage your Purchase Agreements.
===========================================================

Manage calls for tenders and blanket orders. Calls for tenders are used to get
competing offers from different vendors and select the best ones. Blanket orders
are agreements you have with vendors to benefit from a predetermined pricing.

## Dependencies
- `purchase`

## Models
- `product`
- `purchase`
- `purchase_requisition`
- `res_config_settings`

## Data Files
- `security/purchase_requisition_security.xml`
- `security/ir.model.access.csv`
- `data/purchase_requisition_data.xml`
- `views/product_views.xml`
- `views/purchase_views.xml`
- `views/purchase_requisition_views.xml`
- `views/res_config_settings_views.xml`
- `report/purchase_requisition_report.xml`
- `report/report_purchaserequisition.xml`
- `wizard/purchase_requisition_alternative_warning.xml`
- `wizard/purchase_requisition_create_alternative.xml`

## Demo Files
- `data/purchase_requisition_demo.xml`

## Security
- `ir.model.access.csv`
- `purchase_requisition_security.xml`

## Views
- `product_views.xml`
- `purchase_requisition_views.xml`
- `purchase_views.xml`
- `res_config_settings_views.xml`

## Wizards
- `__init__.py`
- `purchase_requisition_alternative_warning.py`
- `purchase_requisition_alternative_warning.xml`
- `purchase_requisition_create_alternative.py`
- `purchase_requisition_create_alternative.xml`

## Reports
- `purchase_requisition_report.xml`
- `report_purchaserequisition.xml`

## Asset Bundles
- `web.assets_backend` (4 entries)

## Install Settings
- **Installable:** `True`
- **Auto-install:** `False`
- **Application:** `False`
