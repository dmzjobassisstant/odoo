# google_account Requirements

## Module Overview
- **Name**: Google Users
- **Category**: Hidden/Tools
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: N/A

## Dependencies
- `base_setup`

## Description
Adds Google user functionality to res.users.

## External Services / API
- Google OAuth 2.0 API
  - Auth endpoint: `https://...auth`
  - Token endpoint: `https://...oken`
  - API Base URL: `https://www.googleapis.com`
- Requires `google_service` abstract model providing:
  - Token refresh functionality
  - HTTP request handling to Google APIs

## Configuration Parameters (ir.config_parameter)
- `google_{service}_client_id` - Google OAuth client ID per service
- `google_{service}_client_secret` - Google OAuth client secret per service

## Security
- Access to tokens/secrets restricted to `base.group_system`
- Client secrets are masked in logs (only first 4 chars visible)

## Models
- `google.service` (abstract) - Google OAuth service abstraction
  - `_get_client_id()` - Get Google client ID
  - `_get_authorize_uri()` - Build OAuth authorization URL
  - `_get_google_tokens()` - Exchange auth code for tokens
  - `_refresh_google_token()` - Refresh access token
  - `_do_request()` - Execute Google API requests
