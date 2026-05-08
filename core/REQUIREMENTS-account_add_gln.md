# Requirements: account_add_gln

## Module: account_add_gln (Add Partner GLN)

**Category:** Accounting/Accounting  
**Version:** 1.0  
**Author:** Odoo S.A.  
**License:** LGPL-3  

### Dependencies

- `account`

### External Dependencies

None

### Data Files

- `views/res_partner_views.xml`

### Assets

None

### Hooks

None

### Notes

- Installable: True
- Auto-install: True
- Category: Accounting/Accounting
- Summary: This module adds the Global Location Number to the partner. Used on delivery addresses, it is used to identify stock locations and is mandatory on the UBL/CII eInvoices (but not only). The module is intended be merged with account, later on, in master.
