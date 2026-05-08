# google_gmail Requirements

## Module Overview
- **Name**: Google Gmail
- **Category**: Hidden
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.2
- **Auto-install**: True

## Dependencies
- `mail`

## Description
Gmail support for incoming/outgoing mail servers using OAuth authentication.

## External Services / API
- Gmail OAuth 2.0
- IMAP over SSL (port 993)
- OAuth2 XOAUTH2 authentication mechanism

## Configuration Parameters (ir.config_parameter)
- `google_gmail_client_id` - Gmail OAuth Client ID
- `google_gmail_client_secret` - Gmail OAuth Client Secret

## Models
- `fetchmail.server` - Extended with Gmail support
  - `server_type` adds 'gmail' option with 'Gmail OAuth Authentication'
  - `google_gmail_refresh_token` - OAuth refresh token
  - `google_gmail_access_token` - OAuth access token
  - `google_gmail_access_token_expiration` - Token expiry time

- `ir.mail_server` - Extended with Gmail OAuth

- `res.users` - Extended with Gmail OAuth fields

## Key Features
- SSL required for Gmail servers (port 993)
- Default server: `imap.gmail.com`
- Uses OAuth2 instead of password authentication
- Supports both incoming (fetchmail) and outgoing (ir.mail_server) Gmail servers

## Views
- `views/fetchmail_server_views.xml`
- `views/ir_mail_server_views.xml`
- `views/res_config_settings_views.xml`
- `views/templates.xml`
