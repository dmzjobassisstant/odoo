# Requirements: account_tax_python

## Module: account_tax_python (Define Taxes as Python Code)

**Category:** Accounting/Accounting  
**Version:** 1.0  
**Author:** Odoo S.A.  
**License:** LGPL-3  

### Dependencies

- `account`

### External Dependencies

None

### Data Files

- `views/account_tax_views.xml`

### Assets

**web.assets_backend:**
- `account_tax_python/static/src/helpers/*.js`

**web.assets_frontend:**
- `account_tax_python/static/src/helpers/*.js`

### Hooks

None

### Notes

- Category: Accounting/Accounting
- Summary: Use python code to define taxes
- Description: A tax defined as python code consists of two snippets of python code which are executed in a local environment containing data such as the unit price, product or partner. "Applicable Code" defines if the tax is to be applied. "Python Code" defines the amount of the tax.
