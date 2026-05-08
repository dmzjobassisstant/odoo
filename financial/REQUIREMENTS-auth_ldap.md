# Requirements: auth_ldap

## Module Overview

- **Name**: Authentication via LDAP
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Auto-install**: No

## Depends

- `base`
- `base_setup`

## External Dependencies

- **Python**: `python-ldap`
- **APT**: `python3-ldap`

## Data Files

- `views/ldap_installer_views.xml`
- `security/ir.model.access.csv`
- `views/res_config_settings_views.xml`

## Models

### `res.company.ldap`

Manages LDAP server configuration and user authentication.

**Key Fields**:
- `sequence` — ordering field (default: 10)
- `company` — `res.company`, required, cascade delete
- `ldap_server` — LDAP server address, required, default `127.0.0.1`
- `ldap_server_port` — LDAP server port, required, default 389
- `ldap_binddn` — Bind DN for LDAP queries (optional, anonymous if empty)
- `ldap_password` — Bind password
- `ldap_filter` — LDAP filter string with `%s` placeholder(s) for login; must return exactly one result
- `ldap_base` — DN of user search scope, required
- `user` — `res.users` template user to copy for new users
- `create_user` — Boolean, auto-create local users for LDAP-authenticated users (default: True)
- `ldap_tls` — Boolean, use STARTTLS for secure connections

**Key Methods**:
- `_get_ldap_dicts()` — retrieve all LDAP configs as dicts
- `_connect(conf)` — open LDAP connection (ldap:// URI, handles referrals, TLS)
- `_get_entry(conf, login)` — look up user DN/entry by login using filter
- `_authenticate(conf, login, password)` — bind as user to verify password; returns entry or False
- `_query(conf, filter, retrieve_attributes)` — execute LDAP search as bind DN
- `_map_ldap_attributes(conf, login, ldap_entry)` — map LDAP attributes to `res.users` values
- `_get_or_create_user(conf, login, ldap_entry)` — find or create local Odoo user from LDAP entry
- `_change_password(conf, login, old_passwd, new_passwd)` — change LDAP password via `passwd_s`
- `test_ldap_connection()` — test connection with current config, returns notification action

## Security

- `security/ir.model.access.csv` — standard model access control

## Notes

- Multiple LDAP configurations can be stacked per company via `sequence` ordering
- Prevents empty-password unauthenticated bind attacks
- Supports `auth_ldap.disable_chase_ref` ir.config_parameter to disable referral chasing
