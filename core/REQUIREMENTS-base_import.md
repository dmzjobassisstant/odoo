# Requirements: base_import

## Module Details

- **Name**: Base import
- **Category**: Hidden/Tools
- **Version**: 2.0
- **License**: LGPL-3
- **Author**: Odoo S.A.

## Dependencies

- web

## Data Files

- security/ir.model.access.csv

## External Dependencies

None

## Assets

- web.assets_backend: 
  - base_import/static/src/**/*.scss
  - base_import/static/src/**/*.js
  - base_import/static/src/**/*.xml
- web.assets_unit_tests: base_import/static/tests/**/*.test.js

## Auto Install

- True

## Installable

- True

## Description

New extensible file import for Odoo. Re-implements Odoo's file import system in a more extensible manner, allowing users and partners to build their own front-end to import from other file formats (e.g., OpenDocument files).
