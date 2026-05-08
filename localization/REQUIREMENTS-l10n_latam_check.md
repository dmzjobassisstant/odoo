# l10n_latam_check — Third Party and Deferred/Electronic Checks Management

## Module Details
- **Name:** Third Party and Deferred/Electronic Checks Management
- **Version:** 1.0.0
- **Category:** Accounting/Localizations
- **Author:** ADHOC SA
- **License:** LGPL-3

## Description
Own Checks Management:
- Use own checks (not printed, filled manually)
- Deferred/electronic checks
- Check Cash-In Date for post-dated checks

Third Party Checks Management:
- New Third Party Checks (from customers)
- Existing Third Party check tracking (pay vendor, deposit, rejection, return, transfer)

## Dependencies
### Odoo Modules
- `account`
- `base_vat`

## Data Files
- `data/account_payment_method_data.xml`
- `wizards/l10n_latam_payment_mass_transfer_views.xml`
- `security/ir.model.access.csv`
- `security/security.xml`
- `views/account_payment_view.xml`
- `views/l10n_latam_check_view.xml`
- `views/report_payment_receipt_templates.xml`
- `wizards/account_payment_register_views.xml`

## Requirements Summary
- Requires account and base_vat
- Check management for LATAM countries
