# Requirements: account_update_tax_tags

## Module: account_update_tax_tags (Account - Allow updating tax grids)

**Category:** Accounting/Accounting  
**Version:** 1.0  
**Author:** Odoo S.A.  
**License:** LGPL-3  

### Dependencies

- `account`

### External Dependencies

None

### Data Files

- `security/ir.model.access.csv`
- `views/res_config_settings_views.xml`
- `wizard/account_update_tax_tags_wizard.xml`

### Assets

None

### Hooks

None

### Notes

- Category: Accounting/Accounting
- Summary: Allow updating tax grids on existing entries
- Description: This module allows updating tax grids on existing accounting entries. In debug mode a button to update your entries' tax grids will be available in Accounting settings. This is typically useful after some legal changes were done on the tax report, requiring a new tax configuration.
