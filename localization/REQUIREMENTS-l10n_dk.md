# Requirements for l10n_dk

## Module: l10n_dk
**Name:** Denmark - Accounting

### Basic Info
- **Countries:** dk
- **Author:** Odoo House ApS, VK DATA ApS, FlexERP ApS
- **Version:** 1.3
- **License:** LGPL-3
- **Category:** Accounting/Localizations/Account Charts

### Dependencies
- base_iban
- base_vat
- account
- account_edi_ubl_cii

### Auto-installs
- account

### Data Files
- data/account_tax_report_data.xml
- data/account.account.tag.csv
- views/account_journal_views.xml
- views/res_partner_views.xml
- views/res_company_views.xml

### Demo Data
- demo/demo_company.xml

### Description
Localization Module for Denmark - accounting chart for Denmark covering:
- Danish chart of accounts
- Danish VAT (25% moms, 6.25% restaurant moms, reverse charge)
- Accounting groups for EU (business), EU (private), third countries
- Financial reports: Income statement, Balance sheet, VAT settlement
- Anglo-saxon accounting method
