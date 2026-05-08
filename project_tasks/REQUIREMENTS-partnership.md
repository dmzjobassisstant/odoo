# partnership — Requirements

## Module Overview
- **Name**: Partnership / Membership
- **Version**: 1.0
- **Category**: Sales/CRM
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Installable

## Dependencies
- `crm`
- `sale`

## Core Functionality
Manages memberships and partnerships. Allows assigning grades to members/partners with specific pricelists.

## Key Models
- `res.partner.grade` — Partner grade/level (sequence, name, default_pricelist_id, partners_count)
- `res.partner` — Extended with `grade_id` and partnership fields
- `product.pricelist` — Extended for partnership pricing
- `product.template` — Extended for partnership products
- `sale.order` — Extended for partnership logic
- `res.company` — Extended with partnership_label

## Key Features
- Partner grading system (Bronze, Silver, Gold, etc.)
- Per-grade default pricelists
- Partner count tracking per grade
- Partnership menu navigation

## Data Files
- `security/ir.model.access.csv`
- `data/res_partner_grade_data.xml`
- `views/res_config_settings_views.xml`
- `views/res_partner_views.xml`
- `views/res_partner_grade_views.xml`
- `views/product_template_views.xml`
- `views/product_pricelist_views.xml`
- `views/partnership_menu.xml`

## Security
- Access control via `ir.model.access.csv`
