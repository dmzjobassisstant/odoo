# REQUIREMENTS — hr (Employees)

## Module Details
- **Name:** Employees
- **Category:** Human Resources/Employees
- **Version:** 1.1
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Application:** Yes

## Depends
- `base_setup`
- `digest`
- `phone_validation`
- `resource_mail`
- `web`

## Description
Centralize employee information.

## Data Files
- `security/hr_security.xml`
- `security/ir.model.access.csv`
- `data/digest_data.xml`
- `data/report_paperformat.xml`
- `wizard/hr_departure_wizard_views.xml`
- `wizard/hr_contract_template_wizard.views.xml`
- `wizard/mail_activity_schedule_views.xml`
- `wizard/hr_bank_account_allocation_wizard.xml`
- `wizard/hr_bank_account_allocation_wizard_line.xml`
- `views/mail_activity_plan_views.xml`
- `views/hr_version_views.xml`
- `views/hr_contract_template_views.xml`
- `views/hr_departure_reason_views.xml`
- `views/hr_contract_type_views.xml`
- `views/hr_job_views.xml`
- `views/hr_employee_category_views.xml`
- `views/hr_employee_public_views.xml`
- `report/hr_employee_badge.xml`
- `views/hr_employee_views.xml`
- `views/hr_department_views.xml`
- `views/hr_work_location_views.xml`
- `views/hr_views.xml`
- `views/res_config_settings_views.xml`
- `views/res_partner_views.xml`
- `views/res_partner_bank_views.xml`
- `views/discuss_channel_views.xml`
- `views/res_users.xml`
- `views/hr_templates.xml`
- `data/hr_data.xml`

## Demo
- `data/hr_demo.xml`

## Models
- `hr.contract.type`
- `hr.department`
- `hr.departure.reason`
- `hr.employee`
- `hr.employee.category`
- `hr.employee.public`
- `hr.job`
- `hr.work.location`
- `mail.alias`
- `mail.activity.plan` / `mail.activity.plan.template`
- `res.company`
- `res.users`
