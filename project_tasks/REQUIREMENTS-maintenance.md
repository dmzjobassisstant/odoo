# Requirements: maintenance

## Module Overview
- **Name**: Maintenance
- **Version**: 1.0
- **Category**: Supply Chain/Maintenance
- **Website**: https://www.odoo.com/app/maintenance
- **Depends**: `mail`
- **Application**: Yes
- **License**: LGPL-3

## Description
Track equipment and maintenance requests, manage maintenance teams and schedule preventive maintenance.

## Dependencies

### Internal Dependencies
- `mail` - Mail/messaging for notifications

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `maintenance.stage` | Maintenance Stage - pipeline stages |
| `maintenance.equipment.category` | Equipment Category |
| `maintenance.equipment` | Equipment - asset to maintain |
| `maintenance.request` | Maintenance Request - work order |
| `maintenance.team` | Maintenance Team |
| `maintenance.mixin` | Mixin for equipment tracking on any model |

### Equipment Fields
- Serial number tracking
- Cost and warranty tracking
- Vendor/partner management
- MTBF (Mean Time Between Failure) calculation
- MTTR (Mean Time To Repair) calculation
- Maintenance team assignment
- Technician assignment

### Maintenance Request Fields
- Equipment linked
- Category
- Stage with done flag
- Request date and close date
- Maintenance type (preventive/corrective)
- Priority

## Views & Security

### Data Files
- `security/maintenance.xml` - Security rules
- `security/ir.model.access.csv` - Access control
- `data/maintenance_data.xml` - Demo and default data
- `data/mail_activity_type_data.xml` - Activity types
- `data/mail_message_subtype_data.xml` - Message subtypes

### View Files
- `views/maintenance_views.xml`
- `views/mail_activity_views.xml`
- `views/res_config_settings_views.xml`

## Key Features
- Equipment registry with maintenance tracking
- Maintenance request workflow
- Preventive vs corrective maintenance
- Maintenance team management
- Technician assignment
- Maintenance scheduling
- MTBF and MTTR calculations
- Estimated next failure date
- Equipment properties (via PropertiesDefinition)
- Category-based maintenance organization
- Activity-based follow-ups
