# Requirements: analytic

## Module: analytic (Analytic Accounting)

**Category:** Accounting/Accounting  
**Version:** 1.2  
**Author:** Odoo S.A.  
**License:** LGPL-3  

### Dependencies

- `base`
- `mail`
- `uom`

### External Dependencies

None

### Data Files

- `security/analytic_security.xml`
- `security/ir.model.access.csv`
- `views/analytic_line_views.xml`
- `views/analytic_account_views.xml`
- `views/analytic_plan_views.xml`
- `views/analytic_distribution_model_views.xml`
- `data/analytic_data.xml`

### Demo Data

- `data/analytic_account_demo.xml`

### Assets

**web.assets_backend:**
- `analytic/static/src/components/**/*`
- `analytic/static/src/services/**/*`
- `analytic/static/src/views/**/*`
- *(remove)* `analytic/static/src/views/graph/**`
- *(remove)* `analytic/static/src/views/pivot/**`

**web.assets_backend_lazy:**
- `analytic/static/src/views/graph/**`
- `analytic/static/src/views/pivot/**`

**web.assets_unit_tests:**
- `analytic/static/tests/**/*`

### Hooks

None

### Notes

- Installable: True
- Category: Accounting/Accounting
- Description: Module for defining analytic accounting object. In Odoo, analytic accounts are linked to general accounts but are treated totally independently. So, you can enter various different analytic operations that have no counterpart in the general financial accounts.
