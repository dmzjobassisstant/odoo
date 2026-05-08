# Requirements: account_edi_proxy_client

## Module: account_edi_proxy_client (Proxy features for account_edi)

**Category:** Accounting/Accounting  
**Version:** 1.0  
**Author:** Odoo S.A.  
**License:** LGPL-3  

### Dependencies

- `account`
- `certificate`

### External Dependencies

None

### Data Files

- `security/ir.model.access.csv`
- `security/account_edi_proxy_client_security.xml`
- `views/account_edi_proxy_user_views.xml`

### Assets

None

### Hooks

- `post_init_hook`: `_create_demo_config_param`

### Notes

- Installable: True
- Category: Accounting/Accounting
- Description: This module adds generic features to register an Odoo DB on the proxy responsible for receiving data (via requests from web-services). An edi_proxy_user has a unique identification on a specific proxy type (e.g. l10n_it_edi, peppol) which allows to identify him when receiving a document addressed to him. It is linked to a specific company on a specific Odoo database. Encryption features allows to decrypt all the user's data when receiving it from the proxy. Authentication offers an additional level of security to avoid impersonification, in case someone gains to the user's database.
