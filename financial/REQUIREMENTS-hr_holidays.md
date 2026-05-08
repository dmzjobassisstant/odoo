# REQUIREMENTS — hr_holidays (Time Off)

## Module Details
- **Name:** Time Off
- **Category:** Human Resources/Time Off
- **Version:** 1.6
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Application:** Yes

## Depends
- `hr`
- `calendar`
- `resource`

## Description
Allocate time off and follow leave requests. Manage time off schedule, configure time off types (sickness, paid days, etc.), allocation, reporting (Time Off Summary, Time Off by Department, Time Off Analysis). Synchronization with internal agenda (CRM Meetings) possible.

## Data Files
- `data/report_paperformat.xml`
- `data/mail_activity_type_data.xml`
- `data/mail_message_subtype_data.xml`
- `data/ir_attachment_data.xml`
- `data/hr_leave_type_data.xml`
- `data/ir_cron_data.xml`
- `data/hr_holidays_tour.xml`
- `security/hr_holidays_security.xml`
- `security/ir.model.access.csv`
- `wizard/hr_holidays_cancel_leave_views.xml`
- `wizard/hr_holidays_summary_employees_views.xml`
- `wizard/hr_leave_generate_multi_wizard_views.xml`
- `wizard/hr_leave_allocation_generate_multi_wizard_views.xml`
- `views/resource_views.xml`
- `views/hr_leave_views.xml`
- `views/hr_leave_type_views.xml`
- `views/hr_leave_allocation_views.xml`
- `views/hr_leave_accrual_views.xml`
- `views/hr_leave_mandatory_day_views.xml`
- `views/mail_activity_views.xml`
- `views/calendar_views.xml`
- `report/hr_holidays_templates.xml`
- `report/hr_holidays_reports.xml`
- `report/hr_leave_reports.xml`
- `report/hr_leave_report_calendar.xml`
- `report/hr_leave_employee_type_report.xml`
- `views/hr_views.xml`
- `views/hr_holidays_views.xml`

## Demo
- `data/hr_holidays_demo.xml`

## Models
- `hr.leave`
- `hr.leave.allocation`
- `hr.leave.accrual.plan` / `hr.leave.accrual.plan.level`
- `hr.leave.mandatory.day`
- `hr.leave.type`
- `hr.department`
- `hr.employee`
- `hr.employee.public`
- `calendar.event`
- `resource.resource`
- `mail.activity.type`
