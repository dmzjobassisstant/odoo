# mail_plugin Requirements

## Module Overview
- **Name**: Mail Plugin
- **Category**: Sales/CRM
- **Summary**: Allows integration with mail plugins.
- **Description**: Integrate Odoo with your mailbox, get information about contacts directly inside your mailbox, log content of emails as internal notes.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.0
- **Sequence**: 5
- **Installable**: True

## Technical Details

### Dependencies
- `web`
- `contacts`
- `iap`

### Data Files
- `views/mail_plugin_login.xml`
- `views/res_partner_iap_views.xml`
- `security/ir.model.access.csv`

### Purpose
Integrates Odoo with external mailbox plugins to show contact information and log email content.
