# REQUIREMENTS — hr_org_chart (HR Org Chart)

## Module Details
- **Name:** HR Org Chart
- **Category:** Human Resources
- **Version:** 1.0
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Auto-install:** `['hr']`

## Depends
- `hr`
- `web_hierarchy`

## Description
Org Chart Widget for HR. Extends the employee form with an organizational chart (N+1, N+2, direct subordinates).

## Data Files
- `views/hr_department_views.xml`
- `views/hr_employee_public_views.xml`
- `views/hr_views.xml`

## Models
- `hr.department`
- `hr.employee.public`
