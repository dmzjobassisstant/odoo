# Requirements: barcodes_gs1_nomenclature

## Module Overview
- **Name**: Barcode - GS1 Nomenclature
- **Version**: 1.0
- **Category**: Supply Chain/Inventory
- **Depends**: `barcodes`, `uom`
- **License**: LGPL-3

## Description
Parse barcodes according to GS1-128 specifications.

## Dependencies

### Internal Dependencies
- `barcodes` - Base barcode module
- `uom` - Unit of Measure module

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `barcode.nomenclature` | Extended with GS1 parsing rules |
| `barcode.rule` | Extended with GS1-specific fields |
| `ir.http` | Extended with GS1 barcode handling |

## Views & Security

### Data Files
- `data/barcodes_gs1_rules.xml` - GS1 barcode rules

### View Files
- `views/barcodes_view.xml` - GS1 nomenclature views

## Key Features
- GS1-128 barcode parsing
- GS1 company prefix handling
- GTIN, SSCC, SGTIN parsing from GS1 barcodes
- GS1 application identifiers support
- Unit of measure integration
