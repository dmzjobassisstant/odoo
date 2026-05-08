# Requirements - test_mail

**Module:** Mail Tests  
**Version:** 1.0  
**Category:** Hidden  
**License:** LGPL-3  
**Author:** Odoo S.A.

## Description
This module contains tests related to mail. Those are present in a separate module as it contains models used only to perform tests independently to functional aspects of other models.

## Dependencies
- mail
- test_orm

## Data Files
- security/ir.model.access.csv
- security/test_mail_security.xml
- data/data.xml
- data/mail_template_data.xml
- data/subtype_data.xml

## Assets
- web.assets_unit_tests: test_mail/static/tests/**/*
- web.assets_tests: test_mail/static/tests/tours/*