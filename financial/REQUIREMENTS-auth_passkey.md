# Requirements: auth_passkey

## Module Overview

- **Name**: Passkeys
- **Version**: 1.1
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: True

## Depends

- `base_setup`
- `web`

## External Dependencies

None specified in manifest.

## Data Files

- `views/auth_passkey_key_views.xml`
- `views/auth_passkey_login_templates.xml`
- `views/res_users_identitycheck_views.xml`
- `views/res_users_views.xml`
- `security/ir.model.access.csv`
- `security/security.xml`

## Assets

- `web.assets_backend`: `auth_passkey/static/lib/simplewebauthn.js`, `auth_passkey/static/src/views/*`, `auth_passkey/static/src/scss/res_users.scss`
- `web.assets_frontend`: `auth_passkey/static/lib/simplewebauthn.js`, `auth_passkey/static/src/interactions/*`
- `web.assets_tests`: `auth_passkey/static/tests/*.js`

## Models

### `auth.passkey.key`

Stores passkey credentials per user.

**Key Fields**:
- `name` — Human-readable name, required
- `credential_identifier` — Unique credential ID (base64url), required; group: `base.group_system`
- `public_key` — Stored as `varchar` column; computed/serialized; group: `base.group_system`
- `sign_count` — Signature counter, default 0; group: `base.group_system`
- `create_uid` — `res.users` who created the passkey

**Constraints**:
- `UNIQUE(credential_identifier)` — credential ID must be unique

**Key Methods**:
- `init()` — creates `public_key` column via `ALTER TABLE` if missing (migration-safe)
- `unlink()` — logs deletion with user/IP info
- `_get_session_challenge()` — pops `webauthn_challenge` from session
- `_start_auth()` — generates WebAuthn authentication options, stores challenge in session
- `_verify_auth(auth, public_key, sign_count)` — verifies authentication response using `simplewebauthn`
- `_start_registration()` — generates WebAuthn registration options, stores challenge
- `_verify_registration_options(registration)` — verifies registration response
- `action_delete_passkey()` — deletes passkey (requires identity check, only owner can delete)
- `action_rename_passkey()` — opens rename dialog

### `auth.passkey.key.create` (TransientModel)

Wizard to create a new passkey for the current user.

**Fields**:
- `name` — Name for the passkey, required

**Key Methods**:
- `make_key(registration)` — verifies registration, creates `auth.passkey.key` record with credential ID; stores public key via raw SQL; requires identity check

## Security

- Passkey deletion and creation require identity verification (`@check_identity`)
- Only the creating user can delete their own passkey
- Credential identifiers are hidden from non-system users
