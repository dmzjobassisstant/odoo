# Requirements - test_spreadsheet

**Module:** Spreadsheet Test  
**Version:** 1.0  
**Category:** Hidden  
**License:** LGPL-3  
**Author:** Odoo S.A.

## Description
This module contains tests related to spreadsheet. The modules exposes some mixin that are only implemented in other functional modules. When trying to test a global behavior of the mixin, it makes no sense to test it in each module implementing the mixin but rather test a dummy implementation of the later, hence the need for this test module.

## Dependencies
- spreadsheet

## Data Files
- security/spreadsheet_test_security.xml
- security/ir.model.access.csv