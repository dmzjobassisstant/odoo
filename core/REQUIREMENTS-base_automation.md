# Requirements: base_automation

## Module Details

- **Name**: Automation Rules
- **Category**: Sales/Sales
- **Version**: 1.0
- **License**: LGPL-3
- **Author**: Odoo S.A.

## Dependencies

- base
- digest
- resource
- mail
- sms

## Data Files

- security/ir.model.access.csv
- data/base_automation_data.xml
- data/digest_data.xml
- views/base_automation_views.xml
- views/ir_actions_server_views.xml

## External Dependencies

None

## Assets

- web.assets_backend: base_automation/static/src/**/*
- web.assets_unit_tests: base_automation/static/tests/**/*

## Description

Allows implementing automation rules for any object. Automatically trigger actions for various screens (e.g., lead created by a specific user may be automatically set to a specific Sales Team, or opportunity pending after 14 days might trigger a reminder email).
