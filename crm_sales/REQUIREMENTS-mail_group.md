# mail_group Requirements

## Module Overview
- **Name**: Mail Group
- **Category**: (uses mail, portal)
- **Summary**: Manage your mailing lists
- **Description**: Manage your mailing lists from Odoo. Allows creating moderated mailing groups.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.1

## Technical Details

### Dependencies
- `mail`
- `portal`

### Data Files
- `data/ir_cron_data.xml`
- `data/mail_templates.xml`
- `data/mail_template_data.xml`
- `data/mail_template_email_layouts.xml`
- `data/res_groups.xml`
- `security/ir.model.access.csv`
- `security/mail_group_security.xml`
- `wizard/mail_group_message_reject_views.xml`
- `views/mail_compose_message_views.xml`
- `views/mail_group_member_views.xml`
- `views/mail_group_message_views.xml`
- `views/mail_group_moderation_views.xml`
- `views/mail_group_views.xml`
- `views/mail_group_menus.xml`
- `views/portal_templates.xml`

### Demo Data
- `data/mail_group_demo.xml`

### Assets
- `web.assets_frontend`: SCSS and interactions
- `web.assets_backend`: Backend SCSS

### Models
- `mail.group` - Mailing group model
- `mail.group.member` - Members of mailing groups
- `mail.group.message` - Messages in mailing groups
- `mail.group.moderation` - Moderation settings
