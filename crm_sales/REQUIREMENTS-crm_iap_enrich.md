# Lead Enrichment (crm_iap_enrich)

## Module Details

- **Name**: Lead Enrichment
- **Version**: 1.1
- **Category**: Sales/CRM
- **Summary**: Enrich Leads/Opportunities using email address domain
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Installable**: Not specified
- **Auto Install**: True

## Dependencies

| Type | Module |
|------|--------|
| Core | iap_crm |
| Core | iap_mail |

## External Dependencies

None

## Security

None

## Data Files

- `data/ir_cron.xml`
- `data/ir_action.xml`
- `data/mail_templates.xml`
- `views/crm_lead_views.xml`
- `views/res_config_settings_view.xml`

## Models

- `crm_lead.py`
- `res_config_settings.py`

## Hooks

- Post init hook: `_synchronize_cron`
