# Project Timesheet Holidays Module Requirements

## Module Overview
- **Name**: Timesheet when on Time Off
- **Version**: 1.0
- **Category**: Human Resources
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True
- **Installable**: True

## Dependencies
- `hr_timesheet`
- `hr_holidays`

## Description
Bridge module to integrate leaves in timesheets. Allows automatically logging timesheets when employees are on leaves. Project and task can be configured company-wide.

## Models
- Extends `hr.leave` with timesheet generation
- Extends `account.analytic.line` with holiday link
- Extends `hr.employee` with company-level timesheet settings
- Extends `res.company` with internal project and leave task settings
- Extends `project.task` with timesheet holiday association
- Extends `resource.calendar.leaves` with holiday timesheet generation
- Extends `res.config.settings` with timesheet configuration

## Key Fields
- `hr.leave.timesheet_ids` - One2many to analytic lines (timesheets)
- `res.company.internal_project_id` - Project for timesheet generation
- `res.company.leave_timesheet_task_id` - Task for leave timesheets
- `resource.calendar.leaves` - Calendar leaves with holiday_id

## Key Methods
- `_generate_timesheets()` - Generate timesheets on leave validation
- `_timesheet_prepare_line_values()` - Prepare timesheet line values
- `_check_missing_global_leave_timesheets()` - Check for missing timesheets
- `action_refuse()` - Remove timesheets on refused leave
- `_action_user_cancel()` - Remove timesheets on cancelled leave
- `_force_cancel()` - Force cancel handling
- `write()` - Reevaluate timesheets on leave update

## Hooks
- `post_init` - Post-initialization hook

## Views
- `res_config_settings_views.xml`
- `project_task_views.xml`

## Security
- `ir.model.access.csv` - Model access control

## Demo Data
- `holiday_timesheets_demo.xml`