# Requirements: account_check_printing

## Module: account_check_printing (Check Printing Base)

**Category:** Accounting/Accounting  
**Version:** 1.0  
**Author:** Odoo S.A.  
**License:** LGPL-3  

### Dependencies

- `account`

### External Dependencies

None

### Data Files

- `security/ir.model.access.csv`
- `data/account_check_printing_data.xml`
- `views/account_journal_views.xml`
- `views/account_payment_views.xml`
- `views/res_config_settings_views.xml`
- `wizard/print_prenumbered_checks_views.xml`

### Assets

None

### Hooks

- `post_init_hook`: `create_check_sequence_on_bank_journals`

### Notes

- Installable: True
- Category: Accounting/Accounting
- Summary: Check printing basic features
- Description: This module offers the basic functionalities to make payments by printing checks. It must be used as a dependency for modules that provide country-specific check templates. The check settings are located in the accounting journals configuration page.
