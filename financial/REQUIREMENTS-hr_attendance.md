# REQUIREMENTS — hr_attendance (Attendances)

## Module Details
- **Name:** Attendances
- **Category:** Human Resources/Attendances
- **Version:** 2.0
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Application:** Yes

## Depends
- `hr`
- `barcodes`
- `base_geolocalize`

## Description
Track employee attendance. Keeps account of the attendances of the employees on the basis of the actions (Check in/Check out) performed by them.

## Data Files
- `data/hr_attendance_overtime_ruleset_data.xml`
- `data/hr_attendance_overtime_rule_data.xml`
- `data/hr_attendance_data.xml`
- `security/hr_attendance_security.xml`
- `security/hr_attendance_overtime_ruleset_security.xml`
- `security/ir.model.access.csv`
- `views/hr_attendance_view.xml`
- `views/hr_department_view.xml`
- `views/hr_employee_view.xml`
- `views/hr_employee_public_views.xml`
- `views/res_config_settings_views.xml`
- `views/hr_attendance_kiosk_templates.xml`
- `views/hr_attendance_overtime_rule_views.xml`

## Demo
- `data/hr_attendance_demo.xml`

## Models
- `hr.attendance`
- `hr.attendance.overtime`
- `hr.attendance.overtime.rule`
- `hr.attendance.overtime.ruleset`
- `hr.employee`
- `hr.employee.public`
- `res.company`
- `res.users`

## Hooks
- `post_init_hook`
- `uninstall_hook`
