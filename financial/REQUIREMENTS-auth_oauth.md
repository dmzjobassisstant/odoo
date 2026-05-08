# Requirements: auth_oauth

## Module Overview

- **Name**: OAuth2 Authentication
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: No

## Depends

- `base`
- `web`
- `base_setup`
- `auth_signup`

## External Dependencies

None specified in manifest.

## Data Files

- `data/auth_oauth_data.xml`
- `views/auth_oauth_views.xml`
- `views/res_config_settings_views.xml`
- `views/auth_oauth_templates.xml`
- `security/ir.model.access.csv`

## Assets

- `web.assets_frontend`: `auth_oauth/static/**/*`

## Models

### `auth.oauth.provider`

Configuration for OAuth2 providers (Google, etc.).

**Key Fields**:
- `name` — Provider name (e.g., Google), required
- `client_id` — OAuth client ID (our identifier)
- `auth_endpoint` — Authorization URL (provider's OAuth endpoint), required
- `scope` — OAuth scope, default `openid profile email`
- `validation_endpoint` — UserInfo URL to retrieve user info, required
- `data_endpoint` — Optional endpoint for additional data
- `enabled` — Boolean, allowed state
- `css_class` — CSS class for login button, default `fa fa-fw fa-sign-in text-primary`
- `body` — Login button label text, required, translatable
- `sequence` — Ordering field, default 10
