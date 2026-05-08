# CRM

## Module Details

- **Name**: CRM
- **Version**: 1.9
- **Category**: Sales/CRM
- **Summary**: Track leads and close opportunities
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Website**: https://www.odoo.com/app/crm
- **Application**: Yes
- **Installable**: True
- **Auto Install**: No

## Dependencies

| Type | Module |
|------|--------|
| Core | base_setup |
| Core | sales_team |
| Core | mail |
| Core | calendar |
| Core | resource |
| Core | utm |
| Core | web_tour |
| Core | contacts |
| Core | digest |
| Core | phone_validation |

## External Dependencies

None

## Security

- `security/crm_security.xml`
- `security/ir.model.access.csv`

## Data Files

- `data/crm_lead_merge_template.xml`
- `data/crm_lead_prediction_data.xml`
- `data/crm_lost_reason_data.xml`
- `data/crm_stage_data.xml`
- `data/crm_team_data.xml`
- `data/digest_data.xml`
- `data/ir_action_data.xml`
- `data/ir_cron_data.xml`
- `data/mail_message_subtype_data.xml`
- `data/crm_recurring_plan_data.xml`
- `data/crm_tour.xml`
- `wizard/crm_lead_lost_views.xml`
- `wizard/crm_lead_to_opportunity_views.xml`
- `wizard/crm_lead_to_opportunity_mass_views.xml`
- `wizard/crm_merge_opportunities_views.xml`
- `wizard/crm_lead_pls_update_views.xml`
- `views/calendar_views.xml`
- `views/crm_recurring_plan_views.xml`
- `views/crm_lost_reason_views.xml`
- `views/crm_stage_views.xml`
- `views/crm_lead_views.xml`
- `views/crm_team_member_views.xml`
- `views/digest_views.xml`
- `views/mail_activity_plan_views.xml`
- `views/mail_activity_views.xml`
- `views/res_config_settings_views.xml`
- `views/res_partner_views.xml`
- `views/utm_campaign_views.xml`
- `report/crm_activity_report_views.xml`
- `report/crm_opportunity_report_views.xml`
- `views/crm_team_views.xml`
- `views/crm_menu_views.xml`
- `views/crm_helper_templates.xml`

## Demo Data

- `data/crm_team_demo.xml`
- `data/crm_stage_demo.xml`
- `data/mail_template_demo.xml`
- `data/crm_team_member_demo.xml`
- `data/crm_lead_demo.xml`

## Models

- `crm_lead.py` - CRM Lead (Opportunities and Leads)
- `crm_lead_scoring_frequency.py` - Lead Scoring Frequency
- `crm_lost_reason.py` - Lost Reason
- `crm_recurring_plan.py` - Recurring Plan
- `crm_stage.py` - CRM Stage
- `crm_team.py` - CRM Team
- `crm_team_member.py` - CRM Team Member
- `calendar.py` - Calendar Integration
- `digest.py` - Digest (KPI) Integration
- `ir_config_parameter.py` - IR Config Parameter
- `mail_activity.py` - Mail Activity
- `res_config_settings.py` - Res Config Settings
- `res_partner.py` - Partner Integration
- `res_users.py` - User Integration
- `utm.py` - UTM Integration

## Assets

- `web.assets_backend`: `crm/static/src/**` (partial: forecast_graph and forecast_pivot excluded)
- `web.assets_backend_lazy`: forecast graph and pivot modules
- `web.assets_tests`: `crm/static/tests/tours/**/*`
- `web.assets_unit_tests`: mock server and test files

## Hooks

- Post init hook: `_post_init_hook`
