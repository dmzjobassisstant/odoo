# l10n_vn — Vietnam - Accounting

## Metadata
- **Name**: Vietnam - Accounting
- **Version**: 2.0.3
- **Author**: General Solutions
- **Category**: Accounting/Localizations/Account Charts
- **Website**: https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations/vietnam.html
- **License**: LGPL-3

## Description
This is the module to manage the accounting chart, bank information for Vietnam in Odoo.

- This module applies to companies based in Vietnamese Accounting Standard (VAS) with Chart of account under Circular No. 200/2014/TT-BTC
- Add Vietnamese bank information (like name, bic ..) as announced and yearly updated by State Bank of Viet Nam (https://sbv.gov.vn/webcenter/portal/en/home/sbv/paytreasury/bankidno)
- Add VietQR feature for invoice

**Credits:**
- General Solutions
- Trobz
- Jean Nguyen - The Bean Family (https://github.com/anhjean/vietqr) for VietQR

## Dependencies
- `account_qr_code_emv`
- `base_iban`
- `account`

## Auto-install
- `account`

## Data Files
- `data/account_tax_report_data.xml`
- `views/account_move_views.xml`
- `views/res_bank_views.xml`

## Demo
- `demo/demo_company.xml`
