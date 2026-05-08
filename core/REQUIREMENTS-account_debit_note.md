# Requirements: account_debit_note

## Module: account_debit_note (Debit Notes)

**Category:** Accounting/Accounting  
**Version:** 1.0  
**Author:** Odoo S.A.  
**License:** LGPL-3  

### Dependencies

- `account`

### External Dependencies

None

### Data Files

- `wizard/account_debit_note_view.xml`
- `views/account_move_view.xml`
- `views/account_journal_views.xml`
- `security/ir.model.access.csv`

### Assets

None

### Hooks

None

### Notes

- Installable: True
- Category: Accounting/Accounting
- Summary: Debit Notes
- Description: In a lot of countries, a debit note is used as an increase of the amounts of an existing invoice or in some specific cases to cancel a credit note. It is like a regular invoice, but we need to keep track of the link with the original invoice. The wizard used is similar as the one for the credit note.
