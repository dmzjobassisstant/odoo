# Requirements for l10n_eg_edi_eta

## Module: l10n_eg_edi_eta
**Name:** Egypt E-Invoicing

### Basic Info
- **Countries:** eg
- **Author:** Odoo S.A., Plementus
- **Version:** 0.2
- **License:** LGPL-3
- **Category:** account

### Dependencies
- account_edi
- l10n_eg

### Data Files
- data/account_edi_data.xml
- data/l10n_eg_edi.activity.type.csv
- data/l10n_eg_edi.uom.code.csv
- data/uom.uom.csv
- security/ir.model.access.csv
- security/eta_thumb_drive_security.xml
- views/uom_uom_view.xml
- views/account_move_view.xml
- views/account_journal_view.xml
- views/eta_thumb_drive.xml
- views/product_template_views.xml
- views/res_config_settings_view.xml
- views/report_invoice.xml
- data/res_country_data.xml

### Assets
- web.assets_backend: l10n_eg_edi_eta/static/src/**/*.js

### External Dependencies
- Python: asn1crypto
- Apt: python3-asn1crypto

### Description
Integrates with the ETA portal to automatically send and sign Invoices to the Tax Authority.
