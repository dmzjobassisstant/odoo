# Requirements: barcodes

## Module Overview
- **Name**: Barcode
- **Version**: 2.0
- **Category**: Supply Chain/Inventory
- **Depends**: `web`
- **License**: LGPL-3

## Description
Scan and parse barcodes for inventory and product tracking.

## Dependencies

### Internal Dependencies
- `web` - Web module for assets

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `barcode.nomenclature` | Barcode Nomenclature - rules for barcode parsing |
| `barcode.rule` | Barcode Rule - pattern matching rules |
| `res.company` | Extended with default nomenclature |
| `ir.http` | Extended with barcode scanning |
| `barcode.events.mixin` | Mixin for barcode scan handling |

## Views & Security

### Data Files
- `data/barcodes_data.xml` - Default nomenclature and rules
- `views/barcodes_view.xml` - Nomenclature configuration view
- `security/ir.model.access.csv` - Access control

## Key Features
- Barcode nomenclature management
- Pattern-based barcode parsing
- UPC/EAN conversion settings
- GS1 barcode parsing support
- RFID URI parsing (lgtin, sgtin, sscc)
- Barcode scan event handling
- Default nomenclature assignment per company
- Product identification via barcode
- Lot/serial number from barcode
