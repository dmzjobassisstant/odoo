# Requirements: account_peppol

## Module: account_peppol (Peppol)

**Category:** Accounting/Accounting  
**Version:** 1.2  
**Author:** Odoo S.A.  
**License:** LGPL-3  

### Dependencies

- `account_edi_proxy_client`
- `account_edi_ubl_cii`

### External Dependencies

**Python:**
- `phonenumbers`

**APT (Debian/Ubuntu):**
- `python3-phonenumbers`

### Countries

- at, be, ch, cy, cz, de, dk, ee, es, fi, fr, gr, ie, is, it, lt, lu, lv, mt, nl, no, pl, pt, ro, se, si

### Data Files

- `data/cron.xml`
- `data/mail_templates_email_layouts.xml`
- `data/res_partner_data.xml`
- `security/ir.model.access.csv`
- `views/account_move_views.xml`
- `views/account_portal_templates.xml`
- `views/peppol_authentication_views.xml`
- `views/res_partner_views.xml`
- `views/res_config_settings_views.xml`
- `wizard/peppol_registration_views.xml`
- `wizard/peppol_config_wizard.xml`

### Demo Data

- `demo/account_peppol_demo.xml`

### Cron Jobs

- `ir_cron_peppol_get_new_documents` - PEPPOL: retrieve new documents (every 4 hours)
- `ir_cron_peppol_get_message_status` - PEPPOL: update message status (daily)
- `ir_cron_peppol_get_participant_status` - PEPPOL: update participant status (weekly)
- `ir_cron_peppol_webhook_keepalive` - PEPPOL: webhook keep alive (every 2 weeks)

### Assets

**web.assets_backend:**
- `account_peppol/static/src/components/**/*`
- `account_peppol/static/src/css/**/*`

**web.assets_frontend:**
- `account_peppol/static/src/interactions/*`

### Hooks

- `post_init_hook`: `_account_peppol_post_init`

### Notes

- Auto-install: ['account_edi_ubl_cii'] (auto-install when account_edi_ubl_cii AND one company exists in countries above)
- Category: Accounting/Accounting
- Summary: This module is used to send/receive documents with PEPPOL. Features: Register as a PEPPOL participant, Send and receive documents via PEPPOL network in Peppol BIS Billing 3.0 format.
