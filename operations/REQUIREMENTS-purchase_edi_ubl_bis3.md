# Requirements: purchase_edi_ubl_bis3

**Module:** Import/Export electronic orders with UBL
**Version:** 1.0
**Category:** Supply Chain/Purchase
**Author:** Odoo S.A.
**License:** LGPL-3
**Website:** N/A

## Description
Allows to export and import formats: UBL Bis 3.
When generating the PDF on the order, the PDF will be embedded inside the xml for all UBL formats. This allows the
receiver to retrieve the PDF with only the xml file.

## Dependencies
- `purchase`
- `account_edi_ubl_cii`

## Models
- `purchase_edi_xml_ubl_bis3`
- `purchase_order`

## Install Settings
- **Installable:** `True`
- **Auto-install:** `True`
- **Application:** `False`
