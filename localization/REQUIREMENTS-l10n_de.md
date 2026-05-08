# Requirements for l10n_de

## Module: l10n_de
**Name:** Germany - Accounting

### Basic Info
- **Countries:** de
- **Author:** openbig.org (http://www.openbig.org)
- **Version:** 3.0
- **License:** LGPL-3
- **Category:** Accounting/Localizations/Account Charts

### Dependencies
- base_iban
- base_vat
- l10n_din5008
- account
- account_edi_ubl_cii

### Auto-installs
- account

### Data Files
- data/account_account_tags_data.xml
- views/account_view.xml
- views/res_company_views.xml
- wizard/account_secure_entries_wizard.xml

### Demo Data
- demo/demo_company.xml

### Hooks
- post_init_hook: _post_init_hook

### Description
German accounting chart and localization based on SKR03 or SKR04.
By default, the audit trail is enabled for GoBD compliance.
