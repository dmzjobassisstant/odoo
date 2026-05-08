# privacy_lookup — Requirements

## Module Overview
- **Name**: Privacy
- **Version**: 1.0
- **Category**: Hidden
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Auto-install

## Dependencies
- `mail`

## Core Functionality
Privacy lookup and logging. Helps manage GDPR/data privacy requests by finding records associated with an email/partner and logging privacy-related actions.

## Key Models
- `privacy.log` — Logs privacy-related operations (anonymized name/email, handled by user, execution details)
- `res.partner` — Extended for privacy lookup

## Key Features
- Anonymization of names and emails in logs
- Privacy lookup wizard for finding partner records
- Execution details and notes tracking
- Automatic anonymization on log creation

## Data Files
- `wizard/privacy_lookup_wizard_views.xml`
- `views/privacy_log_views.xml`
- `security/ir.model.access.csv`
- `data/ir_actions_server_data.xml`

## Wizard
- `privacy.lookup.wizard` — Search for partner by email/name and create privacy log entry

## Security
- Access control via `ir.model.access.csv`
