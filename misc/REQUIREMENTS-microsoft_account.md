# microsoft_account Requirements

## Module Overview
- **Name**: Microsoft Users
- **Category**: Hidden/Tools
- **Author**: Odoo S.A.
- **License**: LGPL-3

## Dependencies
- `base_setup`

## Description
Adds Microsoft user functionality to res.users.

## External Services / API
- Microsoft Graph API
  - Auth endpoint: `https://...rize`
  - Token endpoint: `https://...oken`
  - Graph endpoint: `https://graph.microsoft.com`
- OAuth 2.0 protocol

## Configuration Parameters (ir.config_parameter)
- `microsoft_{service}_client_id` - Microsoft OAuth client ID per service
- `microsoft_{service}_client_secret` - Microsoft OAuth client secret per service
- `microsoft_account.auth_endpoint` - Custom auth endpoint
- `microsoft_account.token_endpoint` - Custom token endpoint

## Models
- `microsoft.service` (abstract) - Microsoft OAuth service abstraction
  - `_get_microsoft_client_id()` - Get Microsoft client ID
  - `_get_calendar_scope()` - Returns 'offline_access openid Calendars.ReadWrite'
  - `_get_auth_endpoint()` - Get authorization endpoint
  - `_get_token_endpoint()` - Get token endpoint
  - `_get_authorize_uri()` - Build OAuth authorization URL
  - `_get_microsoft_tokens()` - Exchange auth code for tokens
  - `_refresh_microsoft_token()` - Refresh access token
  - `_do_request()` - Execute Microsoft API requests

- `res.users` - Extended with Microsoft calendar fields:
  - `microsoft_calendar_rtoken` - Refresh token
  - `microsoft_calendar_token` - Access token
  - `microsoft_calendar_token_validity` - Token expiry

## Security
- Access to tokens restricted to `base.group_system`

## Data Files
- `data/microsoft_account_data.xml`
