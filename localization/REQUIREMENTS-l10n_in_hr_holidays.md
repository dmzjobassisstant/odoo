# l10n_in_hr_holidays — India - Time Off

## Module Details
- **Name:** India - Time Off
- **Version:** 1.0
- **Category:** Human Resources/Time Off
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Country:** IN

## Description
Indian Time Off module providing additional features:
- Define Sandwich Leaves on time off type
- Include weekends or holidays in the duration of employee leave request

## Dependencies
### Odoo Modules
- `hr_holidays`

### Auto-Install
- `hr_holidays`

## Data Files
- `security/ir.model.access.csv`
- `security/l10n_in_hr_holidays_security.xml`
- `views/hr_leave_views.xml`
- `views/hr_leave_type_views.xml`
- `views/l10n_in_hr_leave_optional_holiday_views.xml`

## Assets
- `web.assets_backend`: `l10n_in_hr_holidays/static/src/**/*`

## Requirements Summary
- Requires hr_holidays
- India-specific time off rules (sandwich leaves)
