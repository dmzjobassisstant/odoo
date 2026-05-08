# Import electronic orders with UBL (sale_edi_ubl)

## Module Details

- **Name**: Import electronic orders with UBL
- **Version**: 1.0
- **Category**: Sales/Sales
- **Summary**: Electronic ordering - Import UBL Bis 3 format
- **Description**: Allows to import formats: UBL Bis 3. When uploading or pasting Files in order list view with order related data inside XML file or PDF, file with embedded XML data will allow seller to retrieve Order data from Files.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Installable**: True
- **Auto Install**: True

## Dependencies

| Type | Module |
|------|--------|
| Core | sale |
| Core | account_edi_ubl_cii |

## External Dependencies

None

## Security

None

## Data Files

None listed

## Models

- `product_product.py`
- `sale_edi_xml_ubl_bis3.py`
- `sale_order.py`
