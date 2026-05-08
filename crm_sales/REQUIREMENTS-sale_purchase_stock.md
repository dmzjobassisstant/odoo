# sale_purchase_stock Requirements

## Module Overview
- **Name**: MTO Sale <-> Purchase
- **Category**: Sales/Sales
- **Summary**: SO/PO relation in case of MTO
- **Description**: Add relation information between Sale Orders and Purchase Orders if Make to Order (MTO) is activated on one sold product.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.0

## Technical Details

### Dependencies
- `sale_stock`
- `purchase_stock`
- `sale_purchase`
- Installable: True
- Auto-installs: True

### Data Files
- `views/purchase_order_views.xml`

### Purpose
Bridge module that adds relation information between Sale Orders and Purchase Orders when Make to Order (MTO) is activated on products.
