# Requirements: base_iban

## Module Details

- **Name**: IBAN Bank Accounts
- **Category**: Accounting/Accounting
- **Version**: 1.0
- **License**: LGPL-3
- **Author**: Odoo S.A.

## Dependencies

- account
- web

## Data Files

- views/partner_view.xml
- views/setup_wizards_view.xml
- data/res_partner_bank_demo.xml (demo)

## External Dependencies

None

## Assets

- web.assets_backend: base_iban/static/src/components/**/*
- web.assets_unit_tests: base_iban/static/src/tests/**/*

## Description

Installs the base for IBAN (International Bank Account Number) bank accounts and checks for its validity. Provides ability to extract the correctly represented local accounts from IBAN accounts with a single statement.
