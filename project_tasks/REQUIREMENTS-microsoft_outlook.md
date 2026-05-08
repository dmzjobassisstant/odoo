# microsoft_outlook — Requirements

## Module Overview
- **Name**: Microsoft Outlook
- **Version**: 1.1
- **Category**: Hidden
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Auto-install

## Dependencies
- `mail`

## Core Functionality
Adds Outlook OAuth authentication support for incoming/outgoing mail servers. Enables sending email via SMTP with OAuth2 (XOAUTH2) authentication protocol.

## Key Models
- `ir.mail_server` — Extended with Outlook OAuth authentication (`smtp_authentication = 'outlook'`)
- `microsoft.outlook.mixin` — Mixin providing OAuth token management
- `fetchmail.server` — Extended for incoming mail via Outlook

## Key Features
- Outlook OAuth2 SMTP authentication
- TLS (STARTTLS) required connection security
- Auto-configuration of smtp.outlook.com host and port 587
- Token refresh mechanism for OAuth tokens

## Views
- `views/fetchmail_server_views.xml`
- `views/ir_mail_server_views.xml`
- `views/res_config_settings_views.xml`
- `views/templates.xml`

## Constraints
- SMTP password must be empty for Outlook servers
- Encryption must be `starttls`
- Username must match the Outlook/Office365 email address

## External Dependencies
- `base64` — For OAuth2 auth string encoding
