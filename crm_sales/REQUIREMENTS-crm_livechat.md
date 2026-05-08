# CRM Livechat (crm_livechat)

## Module Details

- **Name**: CRM Livechat
- **Version**: Not specified
- **Category**: Sales/CRM
- **Summary**: Create lead from livechat conversation
- **Description**: Create new lead with using /lead command in the channel
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto Install**: True

## Dependencies

| Type | Module |
|------|--------|
| Core | crm |
| Core | im_livechat |

## External Dependencies

None

## Security

- `security/crm_livechat_security.xml`

## Data Files

- `data/utm_data.xml`
- `data/crm_livechat_chatbot_data.xml`
- `views/chatbot_script_views.xml`
- `views/chatbot_script_step_views.xml`
- `views/crm_lead_views.xml`
- `views/discuss_channel_views.xml`

## Models

- `chatbot_script.py`
- `chatbot_script_step.py`
- `crm_lead.py`
- `discuss_channel.py`
- `res_users.py`

## Assets

- `web.assets_backend`: `crm_livechat/static/src/core/**/*`
- `web.assets_unit_tests`: `crm_livechat/static/tests/**/*` (tours excluded)
- `im_livechat.assets_livechat_support_tours`: `crm_livechat/static/tests/tours/support/*`
- `im_livechat.embed_assets_unit_tests_setup`: partial (web/**/* removed)
