# Requirements: account_edi

## Module: account_edi (Import/Export Invoices From XML/PDF)

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
- `views/account_edi_document_views.xml`
- `views/account_move_views.xml`
- `views/account_journal_views.xml`
- `data/cron.xml`

### Security

Record rules defined in `security/ir.model.access.csv`:
- `account.edi.format` - readonly for base.group_user, full access for account.group_account_invoice
- `account.edi.document` - readonly for base.group_user, full access for account.group_account_invoice

### Assets

None

### Hooks

None

### Notes

- Installable: True
- Category: Accounting/Accounting
- Summary: Electronic Data Interchange - EDI is the electronic interchange of business information using a standardized format. This is the base module for import and export of invoices in various EDI formats, and the transmission of said documents to various parties involved in the exchange (other company, governments, etc.)
