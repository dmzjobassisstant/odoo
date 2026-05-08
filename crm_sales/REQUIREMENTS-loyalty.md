# loyalty Requirements

## Module Overview
- **Name**: Coupons & Loyalty
- **Category**: Sales
- **Summary**: Use discounts, gift card, eWallets and loyalty programs in different sales channels
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.0

## Technical Details

### Dependencies
- `product`
- `portal`
- `account`
- Installable: True

### Data Files
- `security/ir.model.access.csv`
- `security/loyalty_security.xml`
- `report/loyalty_report_templates.xml`
- `report/loyalty_report.xml`
- `data/mail_template_data.xml`
- `data/loyalty_data.xml`
- `wizard/loyalty_card_update_balance_views.xml`
- `wizard/loyalty_generate_wizard_views.xml`
- `views/loyalty_card_views.xml`
- `views/loyalty_history_views.xml`
- `views/loyalty_mail_views.xml`
- `views/loyalty_program_views.xml`
- `views/loyalty_reward_views.xml`
- `views/loyalty_rule_views.xml`
- `views/portal_templates.xml`
- `views/res_partner_views.xml`

### Demo Data
- `data/loyalty_demo.xml`

### Assets
- `web.assets_backend`: JS, SCSS, XML files (backend)
- `web.assets_web_dark`: Dark mode SCSS files
- `web.assets_frontend`: JS, interactions (portal/frontend)

### Models
- `loyalty.card` - Loyalty cards (coupons, gift cards, eWallets)
- `loyalty.program` - Loyalty program definitions
- `loyalty.reward` - Rewards given by loyalty programs
- `loyalty.rule` - Rules that trigger loyalty benefits
- `loyalty.history` - History of loyalty point changes
- `product.template` - Extended with loyalty program linkage
- `product.product` - Extended with loyalty linkage
- `res.partner` - Extended with loyalty card association
