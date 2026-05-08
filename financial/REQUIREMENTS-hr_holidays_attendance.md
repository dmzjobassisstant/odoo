# REQUIREMENTS — hr_holidays_attendance (HR Attendance Holidays)

## Module Details
- **Name:** HR Attendance Holidays
- **Category:** Human Resources
- **Version:** 1.0
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Auto-install:** True

## Depends
- `hr_attendance`
- `hr_holidays`

## Description
Convert employee's extra hours to leave allocations.

## Data Files
- `security/ir.model.access.csv`
- `views/hr_leave_allocation_views.xml`
- `views/hr_leave_type_views.xml`
- `views/hr_leave_views.xml`
- `views/hr_employee_views.xml`
- `views/hr_leave_accrual_level_views.xml`
- `views/hr_leave_attendance_report_views.xml`
- `views/hr_attendance_overtime_views.xml`
- `data/hr_holidays_attendance_data.xml`

## Models
- `hr.leave.allocation`
- `hr.leave.type`
- `hr.leave`
- `hr.employee`
- `hr.leave.accrual.level`
- `hr.leave.attendance.report`
- `hr.attendance.overtime`
