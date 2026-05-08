# Requirements - test_mail_full

**Module:** Mail Tests (Full)  
**Version:** 1.0  
**Category:** Hidden  
**License:** LGPL-3  
**Author:** Odoo S.A.

## Description
This module contains tests related to various mail features and mail-related sub modules. Those tests are present in a separate module as it contains models used only to perform tests independently to functional aspects of real applications.

## Dependencies
- mail
- mail_bot
- portal
- rating
- mass_mailing
- mass_mailing_sms
- phone_validation
- sms
- test_mail
- test_mail_sms
- test_mass_mailing

## Data Files
- data/mail_message_subtype_data.xml
- security/ir.model.access.csv
- security/ir_rule_data.xml
- views/test_portal_template.xml

## Assets
- web.assets_unit_tests: test_mail_full/static/tests/**/*
- web.assets_tests: test_mail_full/static/tests/tours/**/*