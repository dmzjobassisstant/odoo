# Lead Generation (crm_iap_mine)

## Module Details

- **Name**: Lead Generation
- **Version**: 1.2
- **Category**: Sales/CRM
- **Summary**: Generate Leads/Opportunities based on country, industries, size, etc.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto Install**: True

## Dependencies

| Type | Module |
|------|--------|
| Core | iap_crm |
| Core | iap_mail |

## External Dependencies

None

## Security

- `security/ir.model.access.csv`

## Data Files

- `data/crm.iap.lead.industry.csv`
- `data/crm.iap.lead.role.csv`
- `data/crm.iap.lead.seniority.csv`
- `data/mail_template_data.xml`
- `data/ir_sequence_data.xml`
- `views/crm_lead_views.xml`
- `views/crm_iap_lead_mining_request_views.xml`
- `views/res_config_settings_views.xml`
- `views/mail_templates.xml`
- `views/crm_menus.xml`

## Models

- `crm_iap_lead_helpers.py`
- `crm_iap_lead_industry.py`
- `crm_iap_lead_mining_request.py`
- `crm_iap_lead_role.py`
- `crm_iap_lead_seniority.py`
- `crm_lead.py`

## Assets

- `web.assets_backend`: `crm_iap_mine/static/src/js/**/*`
