# REQUIREMENTS — hr_timesheet (Task Logs / Timesheets)

## Module Details
- **Name:** Task Logs
- **Category:** Services/Timesheets
- **Version:** 1.0
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Application:** Yes

## Depends
- `hr`
- `hr_hourly_cost`
- `analytic`
- `project`
- `uom`

## Description
Timesheet system. Each employee can encode and track their time spent on different projects. Integrated with cost accounting module for management by affair.

## Data Files
- `security/hr_timesheet_security.xml`
- `security/ir.model.access.csv`
- `security/ir.model.access.xml`
- `data/digest_data.xml`
- `views/hr_timesheet_views.xml`
- `views/res_config_settings_views.xml`
- `views/project_project_views.xml`
- `views/project_task_views.xml`
- `views/project_task_portal_templates.xml`
- `views/hr_timesheet_portal_templates.xml`
- `report/hr_timesheet_report_view.xml`
- `report/project_report_view.xml`
- `report/report_timesheet_templates.xml`
- `views/hr_department_views.xml`
- `views/hr_employee_views.xml`
- `views/hr_employee_public_views.xml`
- `data/hr_timesheet_data.xml`
- `views/project_task_sharing_views.xml`
- `views/project_update_views.xml`
- `wizard/hr_employee_delete_wizard_views.xml`
- `views/hr_timesheet_menus.xml`

## Demo
- `data/hr_timesheet_demo.xml`

## Models
- `account.analytic.line`
- `project.project`
- `project.task`
- `project.update`
- `project.collaborator`
- `hr.employee`
- `hr.employee.public`
- `uom.uom`
- `res.company`

## Hooks
- `_pre_init_hook`
- `create_internal_project` (post_init)
- `_uninstall_hook`
