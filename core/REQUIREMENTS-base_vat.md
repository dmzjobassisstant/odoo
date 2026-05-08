# Requirements: base_vat

## Module Details

- **Name**: VAT Number Validation
- **Category**: Accounting/Accounting
- **Version**: 2.0
- **License**: LGPL-3
- **Author**: Odoo S.A.

## Dependencies

- account

## Data Files

- views/res_config_settings_views.xml
- views/res_partner_views.xml

## External Dependencies

None

## Description

VAT validation for Partner's VAT numbers. After installing this module, values entered in the VAT field of Partners will be validated for all supported countries. The country is inferred from the 2-letter country code that prefixes the VAT number.

Supports two validation levels:
1. Simple off-line check using known validation rules for the country (default)
2. VAT VIES Check option - online verification via EU VIES database (when enabled in company settings)

Supported countries include EU countries and non-EU countries such as Chile, Colombia, Mexico, Norway, and Russia.
