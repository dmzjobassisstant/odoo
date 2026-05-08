# Requirements for l10n_ec

## Module: l10n_ec
**Name:** Ecuadorian Accounting

### Basic Info
- **Countries:** ec
- **Author:** TRESCLOUD (https://trescloud.com)
- **Version:** 3.9
- **License:** LGPL-3
- **Category:** Accounting/Localizations/Account Charts
- **Maintainer:** TRESCLOUD

### Dependencies
- base
- base_iban
- account_debit_note
- l10n_latam_invoice_document
- l10n_latam_base
- account

### Auto-installs
- account

### Data Files
- security/ir.model.access.csv
- data/account_tax_report_data.xml
- data/res.bank.csv
- data/l10n_latam_identification_type_data.xml
- data/res_partner_data.xml
- data/l10n_latam.document.type.csv
- data/l10n_ec.sri.payment.csv
- views/root_sri_menu.xml
- views/account_tax_view.xml
- views/l10n_latam_document_type_view.xml
- views/l10n_ec_sri_payment.xml
- views/account_journal_view.xml
- views/res_partner_view.xml

### Demo Data
- demo/demo_company.xml

### Description
Adds accounting features for Ecuadorian localization compliant with SRI and Super Intendencia de Compañías.

Includes:
- Ecuadorian chart of accounts
- Taxes, tax tags, and tax groups
- Fiscal positions
- Document types (41 purchase document types)
- Identification types
- Ecuador banks
- Partners: Consumidor Final, SRI, IESS, VAT validation
