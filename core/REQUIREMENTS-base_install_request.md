# Requirements: base_install_request

## Module Details

- **Name**: Base - Module Install Request
- **Category**: Hidden
- **Version**: 1.0
- **License**: LGPL-3
- **Author**: Odoo S.A.

## Dependencies

- mail

## Data Files

- security/ir.model.access.csv
- wizard/base_module_install_request_views.xml
- data/mail_template_data.xml
- data/mail_templates_module_install.xml
- views/ir_module_module_views.xml

## External Dependencies

None

## Auto Install

- True

## Post Init Hook

- _auto_install_apps

## Description

Allow internal users requesting a module installation.
