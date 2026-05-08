# sales_team Requirements

## Module Overview
- **Name**: Sales Teams
- **Category**: Sales/Sales
- **Summary**: Sales Teams
- **Description**: Using this application you can manage Sales Teams with CRM and/or Sales
- **Website**: https://www.odoo.com/app/crm
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.1

## Technical Details

### Dependencies
- `base`
- `mail`

### Data Files
- `security/sales_team_security.xml`
- `security/ir.model.access.csv`
- `data/crm_team_data.xml`
- `views/crm_tag_views.xml`
- `views/crm_team_views.xml`
- `views/crm_team_member_views.xml`
- `views/mail_activity_views.xml`

### Demo Data
- `data/crm_team_demo.xml`
- `data/crm_tag_demo.xml`

### Assets
- `web.assets_backend`: All static src files
- `web.assets_unit_tests`: Unit tests

### Installable
- True

### Models
- `crm.team` - Sales team model
- `crm.team.member` - Sales team member model
- `crm.tag` - CRM tags for lead/opportunity categorization
- `res.users` - Extended with sales team membership
