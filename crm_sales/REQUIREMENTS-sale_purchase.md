# sale_purchase Requirements

## Module Overview
- **Name**: Sale Purchase
- **Category**: Sales/Sales
- **Summary**: Sale based on service outsourcing.
- **Description**: Allows the outsourcing of services. This module allows one to sell services provided by external providers and will automatically generate purchase orders directed to the service seller.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.0
- **Website**: https://www.odoo.com/

## Technical Details

### Dependencies
- `sale`
- `purchase`
- Auto-installs: True

### Data Files
- `data/mail_templates.xml`
- `views/product_views.xml`
- `views/sale_order_views.xml`
- `views/purchase_order_views.xml`

### Auto Install
- True

### Models
- `product.template` - Product with vendor/supplier configuration
- `purchase.order` - Extended with sale order reference
- `sale.order` - Extended with linked purchase orders
- `sale.order.line` - Service lines that generate purchase orders
