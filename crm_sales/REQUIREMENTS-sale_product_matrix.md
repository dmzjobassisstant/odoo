# Sale Matrix (sale_product_matrix)

## Module Details

- **Name**: Sale Matrix
- **Version**: 1.0
- **Category**: Sales/Sales
- **Summary**: Add variants to Sales Order through a grid entry
- **Description**: This module allows to fill Sales Order rapidly by choosing product variants quantity through a Grid Entry.
- **Author**: Odoo S.A.
- **License**: LGPL-3

## Dependencies

| Type | Module |
|------|--------|
| Core | sale |
| Core | product_matrix |

## External Dependencies

None

## Security

None

## Data Files

- `views/product_template_views.xml`
- `views/sale_order_views.xml`
- `report/sale_report_templates.xml`

## Demo Data

- `data/product_matrix_demo.xml`

## Models

- `product_template.py`
- `sale_order.py`
- `sale_order_line.py`

## Assets

- `web.assets_backend`: `sale_product_matrix/static/src/**/*`
