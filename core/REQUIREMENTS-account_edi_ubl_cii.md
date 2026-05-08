# Requirements: account_edi_ubl_cii

## Module: account_edi_ubl_cii (Import/Export electronic invoices with UBL/CII)

**Category:** Accounting/Accounting  
**Version:** 1.0  
**Author:** Odoo S.A.  
**License:** LGPL-3  

### Dependencies

- `account`

### External Dependencies

None

### Data Files

- `data/cii_22_templates.xml`
- `views/account_tax_views.xml`
- `views/res_partner_views.xml`

### Assets

**web.assets_backend:**
- `account_edi_ubl_cii/static/src/scss/**/*`

### Hooks

- `uninstall_hook`: `uninstall_hook`

### Notes

- Installable: True
- Auto-install: True
- Category: Accounting/Accounting
- Description: Electronic invoicing module. Allows to export and import formats: E-FFF, UBL Bis 3, EHF3, NLCIUS, Factur-X (CII), XRechnung (UBL). When generating the PDF on the invoice, the PDF will be embedded inside the xml for all UBL formats. E-FFF, NLCIUS and XRechnung (UBL) are only available for Belgian, Dutch and German companies, respectively. UBL Bis 3 is only available for companies which country is present in the EAS list.
