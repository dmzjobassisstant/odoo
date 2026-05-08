# Requirements for l10n_dk_nemhandel

## Module: l10n_dk_nemhandel
**Name:** Denmark EDI - Nemhandel

### Basic Info
- **Author:** Odoo S.A.
- **Version:** 1.0
- **License:** LGPL-3
- **Category:** Accounting/Localizations/EDI

### Dependencies
- account_edi_proxy_client
- account_edi_ubl_cii
- l10n_dk

### Auto-installs
- account_edi_ubl_cii
- l10n_dk

### Data Files
- data/cron.xml
- data/nemhandel_onboarding_tour.xml
- security/ir.model.access.csv
- views/account_journal_dashboard_views.xml
- views/account_move_views.xml
- views/res_partner_views.xml
- views/res_config_settings_views.xml
- wizard/nemhandel_registration_views.xml

### Demo Data
- demo/l10n_dk_nemhandel_demo.xml

### Assets
- web.assets_backend: 
  - l10n_dk_nemhandel/static/src/components/**/*
  - l10n_dk_nemhandel/static/src/tours/nemhandel_onboarding.js

### Hooks
- pre_init_hook: _pre_init_nemhandel
- uninstall_hook: uninstall_hook

### Description
Used to send/receive documents with Nemhandel network in OIOUBL 2.1 format.
