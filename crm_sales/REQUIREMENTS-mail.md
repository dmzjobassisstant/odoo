# mail Requirements

## Module Overview
- **Name**: Discuss
- **Category**: Productivity/Discuss
- **Summary**: Chat, mail gateway and private channels
- **Description**: Chat, mail gateway and private channel. Includes real-time chat/voice/video, mail gateway (POP/IMAP), and Chatter for contextual conversation on documents.
- **Website**: https://www.odoo.com/app/discuss
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.19
- **Sequence**: 145
- **Application**: True
- **Installable**: True

## Technical Details

### Dependencies
- `base`
- `base_setup`
- `bus`
- `web_tour`
- `html_editor`

### Data Files
- `data/mail_groups.xml`
- `wizard/mail_activity_schedule_views.xml`
- `wizard/mail_blacklist_remove_views.xml`
- `wizard/mail_compose_message_views.xml`
- `wizard/mail_template_preview_views.xml`
- `wizard/mail_followers_edit_views.xml`
- `wizard/mail_template_reset_views.xml`
- `views/fetchmail_views.xml`
- `views/ir_cron_views.xml`
- `views/ir_filters_views.xml`
- `views/ir_mail_server_views.xml`
- `views/mail_message_subtype_views.xml`
- `views/mail_tracking_value_views.xml`
- `views/mail_notification_views.xml`
- `views/mail_message_views.xml`
- `views/mail_message_schedule_views.xml`
- `views/mail_mail_views.xml`
- `views/mail_followers_views.xml`
- `views/mail_ice_server_views.xml`
- `views/discuss_channel_member_views.xml`
- `views/discuss_channel_rtc_session_views.xml`
- `views/mail_link_preview_views.xml`
- `views/discuss/discuss_gif_favorite_views.xml`
- `views/discuss_channel_views.xml`
- `views/mail_canned_response_views.xml`
- `views/res_role_views.xml`
- `views/mail_activity_views.xml`
- `views/mail_activity_plan_views.xml`
- `views/mail_activity_plan_template_views.xml`
- `views/res_config_settings_views.xml`
- `data/ir_config_parameter_data.xml`
- `data/res_partner_data.xml`
- `data/mail_message_subtype_data.xml`
- `data/mail_templates_chatter.xml`
- `data/mail_templates_email_layouts.xml`
- `data/mail_templates_mailgateway.xml`
- `data/discuss_channel_data.xml`
- `data/mail_activity_type_data.xml`
- `data/security_notifications_templates.xml`
- `data/ir_cron_data.xml`
- `data/ir_actions_client.xml`
- `security/mail_security.xml`
- `security/ir.model.access.csv`
- `views/discuss_public_templates.xml`
- `views/mail_alias_domain_views.xml`
- `views/mail_alias_views.xml`
- `views/mail_gateway_allowed_views.xml`
- `views/mail_guest_views.xml`
- `views/mail_message_reaction_views.xml`
- `views/mail_templates_public.xml`
- `views/res_users_views.xml`
- `views/res_users_settings_views.xml`
- `views/mail_template_views.xml`
- `views/ir_actions_server_views.xml`
- `views/ir_model_views.xml`
- `views/res_partner_views.xml`
- `views/mail_blacklist_views.xml`
- `views/mail_menus.xml`
- `views/discuss/discuss_menus.xml`
- `views/discuss/discuss_call_history_views.xml`
- `views/res_company_views.xml`
- `views/mail_scheduled_message_views.xml`
- `data/mail_canned_response_data.xml`
- `data/mail_templates_invite.xml`
- `data/web_tour_tour.xml`

### Demo Data
- `demo/mail_activity_demo.xml`
- `demo/discuss_channel_demo.xml`
- `demo/discuss/public_channel_demo.xml`
- `demo/mail_canned_response_demo.xml`

### Assets
- `web._assets_primary_variables`: Primary SCSS variables
- `web.assets_backend`: Full JS/SCSS backend implementation
- `web.assets_backend_lazy`: Activity views (lazy loaded)
- `web.assets_web_dark`: Dark mode SCSS
- `web.assets_frontend`: Format utils for frontend
- `mail.assets_discuss_public_test_tours`: Public discuss tours
- `web.assets_unit_tests`: Unit tests
- `web.assets_tests`: Tour tests
- `web.tests_assets`: Legacy test helpers
- `mail.assets_odoo_sfu`: Odoo SFU for real-time
- `mail.assets_lamejs`: LAME JS for audio
- `mail.assets_message_email`: Email icons
- `mail.assets_public`: Full public assets

### Hooks
- **post_init_hook**: `_mail_post_init`

### Models
- `mail.thread` - Core message threading model
- `mail.message` - Messages in the system
- `mail.mail` - Email mail messages
- `mail.followers` - Followers of documents
- `mail.activity` - Activities on documents
- `mail.activity.plan` - Activity plans
- `mail.activity.type` - Activity types
- `mail.template` - Email templates
- `mail.alias` - Email aliases for incoming mail
- `mail.blacklist` - Email blacklist
- `res.partner` - Extended with mail features
- `res.users` - Extended with mail settings
- `ir.attachment` - Extended with mail features
- `ir.mail_server` - Mail server configuration
- `fetchmail.server` - POP/IMAP server for incoming mail
