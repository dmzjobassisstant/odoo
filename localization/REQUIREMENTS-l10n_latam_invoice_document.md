# l10n_latam_invoice_document — LATAM Document

## Module Details
- **Name:** LATAM Document
- **Version:** 1.0
- **Category:** Accounting/Localizations
- **Author:** ADHOC SA
- **License:** LGPL-3

## Description
Manages document types for Latin American countries (Argentina, Chile, etc.) defined by government fiscal authorities (ARCA, SII). Each document type has rules and sequence numbers integrated with invoice number and journal sequence.

## Dependencies
### Odoo Modules
- `account`
- `account_debit_note`

## Data Files
- `views/account_journal_view.xml`
- `views/account_move_line_view.xml`
- `views/account_move_view.xml`
- `views/l10n_latam_document_type_view.xml`
- `views/report_templates.xml`
- `report/invoice_report_view.xml`
- `wizards/account_move_reversal_view.xml`
- `security/ir.model.access.csv`

## Requirements Summary
- Base module for LATAM document types
- Requires account and account_debit_note
- Document type management for invoices/bills
