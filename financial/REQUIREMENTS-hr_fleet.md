# REQUIREMENTS — hr_fleet (Fleet History)

## Module Details
- **Name:** Fleet History
- **Category:** Human Resources
- **Version:** 1.0
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Auto-install:** True

## Depends
- `hr`
- `fleet`

## Description
Get history of driven cars by employees.

## Data Files
- `security/ir.model.access.csv`
- `security/hr_fleet_security.xml`
- `views/employee_views.xml`
- `views/fleet_vehicle_views.xml`
- `views/fleet_vehicle_cost_views.xml`
- `wizard/hr_departure_wizard_views.xml`
- `data/hr_fleet_data.xml`

## Demo
- `data/hr_fleet_demo.xml`

## Models
- `fleet.vehicle`
- `fleet.vehicle.cost`
- `hr.employee`
