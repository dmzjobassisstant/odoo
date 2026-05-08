# lunch Requirements

## Module Overview
- **Name**: Lunch
- **Category**: Human Resources/Lunch
- **Summary**: Handle lunch orders of your employees
- **Description**: The base module to manage lunch. Handles lunch orders, vendors, meal management, alerts, and employee preferences.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.0
- **Sequence**: 300
- **Application**: True

## Technical Details

### Dependencies
- `mail`

### Data Files
- `security/lunch_security.xml`
- `security/ir.model.access.csv`
- `report/lunch_cashmove_report_views.xml`
- `views/lunch_templates.xml`
- `views/lunch_alert_views.xml`
- `views/lunch_cashmove_views.xml`
- `views/lunch_location_views.xml`
- `views/lunch_orders_views.xml`
- `views/lunch_product_views.xml`
- `views/lunch_supplier_views.xml`
- `views/res_config_settings.xml`
- `views/lunch_views.xml`
- `data/mail_template_data.xml`
- `data/lunch_data.xml`

### Demo Data
- `data/lunch_demo.xml`

### Assets
- `web.assets_backend`: Components, mixins, views, SCSS
- `web.assets_tests`: Tour tests
- `web.assets_unit_tests`: Unit tests

### Installable
- True

### Models
- `lunch.order` - Lunch orders from employees
- `lunch.product` - Products/meals available for lunch
- `lunch.supplier` - Lunch vendors/restaurants
- `lunch.location` - Delivery locations for lunch
- `lunch.cashmove` - Cash movements for lunch account
- `lunch.alert` - Alerts for lunch management
- `lunch.topping` - Extra toppings for lunch products
- `lunch.product.category` - Categories for lunch products
- `res.company` - Extended with lunch settings
