# l10n_tr_nilvera — Türkiye - Nilvera

## Metadata
- **Name**: Türkiye - Nilvera
- **Version**: 1.0
- **Author**: Odoo S.A.
- **Category**: Accounting/Accounting
- **License**: LGPL-3

## Description
Base module containing core functionalities required by other Nilvera modules.

## Dependencies
- `l10n_tr`

## Hooks
- **post_init_hook**: `_l10n_tr_nilvera_post_init`
- **uninstall_hook**: `uninstall_hook`

## Data Files
- `security/ir.model.access.csv`
- `views/res_config_settings_views.xml`
- `views/res_partner_views.xml`
- `data/uom_data.xml`
