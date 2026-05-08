# Requirements: fleet

## Module Overview
- **Name**: Fleet
- **Version**: 0.1
- **Category**: Human Resources/Fleet
- **Website**: https://www.odoo.com/app/fleet
- **Depends**: `base`, `mail`
- **Application**: Yes
- **License**: LGPL-3

## Description
Manage fleet vehicles, contracts, services, costs, and reminders.

## Dependencies

### Internal Dependencies
- `base` - Base module
- `mail` - Mail/messaging for notifications

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `fleet.vehicle` | Vehicle - main fleet entity |
| `fleet.vehicle.model` | Vehicle Model |
| `fleet.vehicle.model.brand` | Vehicle Brand |
| `fleet.vehicle.model.category` | Vehicle Category |
| `fleet.vehicle.state` | Vehicle State (new, in use, etc.) |
| `fleet.vehicle.tag` | Vehicle Tags |
| `fleet.vehicle.log.contract` | Vehicle Contract Log |
| `fleet.vehicle.log.services` | Vehicle Service Log |
| `fleet.vehicle.odometer` | Odometer readings |
| `fleet.vehicle.assignation.log` | Driver Assignment Log |
| `fleet.service.type` | Service Type |
| `mail.activity.type` | Extended for vehicle service reminders |

## Views & Security

### Data Files
- `security/fleet_security.xml` - Fleet security rules
- `security/ir.model.access.csv` - Access control
- `data/fleet_cars_data.xml` - Demo vehicle data
- `data/fleet_data.xml` - Fleet configuration data
- `data/mail_message_subtype_data.xml` - Message subtypes
- `data/mail_activity_type_data.xml` - Service reminder activity types

### View Files
- `views/fleet_vehicle_model_views.xml`
- `views/fleet_vehicle_views.xml`
- `views/fleet_vehicle_cost_views.xml`
- `views/fleet_board_view.xml`
- `views/mail_activity_views.xml`
- `views/res_config_settings_views.xml`
- `views/fleet_vehicle_odometer_report.xml`
- `wizard/fleet_vehicle_send_mail_views.xml`

## Key Features
- Vehicle management with details (license plate, VIN, brand, model)
- Driver assignment and history
- Odometer tracking
- Service logs and reminders
- Contract management (leasing, insurance)
- Contract renewal reminders (due soon, overdue)
- Vehicle cost tracking and analysis
- Vehicle state tracking (new request, in use, damaged, etc.)
- Fleet-specific activity types
- Vehicle tags for categorization
- CO2 emissions tracking
- Vehicle value and depreciation
