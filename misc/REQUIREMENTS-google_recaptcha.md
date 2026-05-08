# google_recaptcha Requirements

## Module Overview
- **Name**: Google reCAPTCHA integration
- **Category**: Hidden
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.0

## Dependencies
- `base_setup`

## Description
Implements reCAPTCHA v3 to prevent bot spam on public modules.

## External Services / API
- Google reCAPTCHA v3 API
  - Verification endpoint: `https://www.recaptcha.net/recaptcha/api/siteverify`
  - Minimum score threshold configurable (default: 0.7)

## Configuration Parameters (ir.config_parameter)
- `enable_recaptcha` - Enable/disable reCAPTCHA (default: True)
- `recaptcha_public_key` - Google reCAPTCHA Site Key
- `recaptcha_private_key` - Google reCAPTCHA Secret Key
- `recaptcha_min_score` - Minimum score threshold (default: 0.7)

## Models
- `ir.http` - Extended with reCAPTCHA verification
  - `_verify_request_recaptcha_token()` - Verify token for an action
  - `_verify_recaptcha_token()` - Call Google API to verify token
  - `session_info()` - Add public key to session info
  - `get_frontend_session_info()` - Add public key to frontend session

## Verification Results
- `is_human` - Token valid and user trustworthy
- `is_bot` - Score below threshold
- `no_secret` - No secret key configured
- `wrong_action` - Action mismatch
- `wrong_token` - Invalid or empty token
- `wrong_secret` - Invalid secret key
- `timeout` - Request or token timeout
- `bad_request` - Malformed request

## Security
- Private key restricted to `base.group_system`
- Public key exposed to frontend session

## Assets
### Frontend (web.assets_frontend)
- `google_recaptcha/static/src/scss/recaptcha.scss`
- `google_recaptcha/static/src/js/recaptcha.js`
- `google_recaptcha/static/src/interactions/**/*`

### Backend (web.assets_backend)
- `google_recaptcha/static/src/xml/recaptcha.xml`

## Views
- `views/res_config_settings_view.xml`
