# contacts — Requirements

## Module Overview
- **Name**: Contacts
- **Version**: 1.0
- **Category**: Sales/CRM
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Application**: True

## Dependencies
- `base`
- `mail`

## Core Functionality
Centralized address book providing a quick view of contacts directory. Tracks vendors, customers, and other contacts. Accessible from the home page.

## Key Models
- `res.partner` — Extended; adds contacts menu to backend root menu

## Key Features
- Contact directory management
- Vendor/customer contact tracking
- Contact menu integration with backend

## Data Files
- `views/contact_views.xml`

## Demo Data
- `data/mail_demo.xml` — Demo contacts data

## Assets
- `web.assets_tests`: Tours from `contacts/static/tests/tours/**/*`

## Security
- Standard Odoo access control (inherited from `base` and `mail`)
