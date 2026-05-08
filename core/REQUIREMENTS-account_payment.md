# Requirements: account_payment

## Module: account_payment (Payment - Account)

**Category:** Accounting/Accounting  
**Version:** 2.0  
**Author:** Odoo S.A.  
**License:** LGPL-3  

### Dependencies

- `account`
- `payment`

### External Dependencies

None

### Data Files

- `data/ir_config_parameter.xml`
- `security/ir.model.access.csv`
- `security/ir_rules.xml`
- `views/account_payment_menus.xml`
- `views/account_portal_templates.xml`
- `views/account_move_views.xml`
- `views/account_journal_views.xml`
- `views/account_payment_views.xml`
- `views/payment_form_templates.xml`
- `views/payment_provider_views.xml`
- `views/payment_transaction_views.xml`
- `wizards/account_payment_register_views.xml`
- `wizards/payment_link_wizard_views.xml`
- `wizards/payment_refund_wizard_views.xml`
- `wizards/res_config_settings_views.xml`

### Assets

**web.assets_unit_tests:**
- `web/static/src/legacy/js/public/minimal_dom.js`
- `account_payment/static/src/interactions/**/*`
- `account_payment/static/tests/interactions/**/*`

**web.assets_frontend:**
- `account_payment/static/src/interactions/**/*`

### Hooks

- `post_init_hook`: `post_init_hook`
- `uninstall_hook`: `uninstall_hook`

### Notes

- Auto-install: ['account']
- Category: Accounting/Accounting
- Summary: Enable customers to pay invoices on the portal and post payments when transactions are processed.
