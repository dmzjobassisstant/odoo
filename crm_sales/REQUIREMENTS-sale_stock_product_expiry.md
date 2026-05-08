# sale_stock_product_expiry Requirements

## Module Overview
- **Name**: Sale Stock Product Expiry
- **Category**: Sales/Sales
- **Description**: Modifications to the forecast widget on SO lines to show fresh stock, i.e. ignoring stock to be removed due to expiration.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 0.1

## Technical Details

### Dependencies
- `sale_stock`
- `product_expiry`
- Installable: True
- Auto-installs: True

### Assets
- `web.assets_tests`: Tour tests
- `web.assets_backend`: Static src files

### Purpose
Modifies the forecast widget on SO lines to show fresh stock (ignoring stock to be removed due to expiration).
