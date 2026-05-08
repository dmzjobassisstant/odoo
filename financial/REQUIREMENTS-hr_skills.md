# REQUIREMENTS — hr_skills (Skills Management)

## Module Details
- **Name:** Skills Management
- **Category:** Human Resources/Employees
- **Version:** 1.0
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Application:** Yes
- **Auto-install:** True

## Depends
- `hr`

## Description
Manage skills, knowledge and resume of your employees.

## Data Files
- `security/ir.model.access.csv`
- `security/hr_skills_security.xml`
- `views/hr_views.xml`
- `views/hr_job_views.xml`
- `views/hr_job_skill_views.xml`
- `data/hr_resume_data.xml`
- `data/hr_skill_data.xml`
- `data/ir_actions_server_data.xml`
- `data/ir_cron_data.xml`
- `data/mail_activity_type_data.xml`
- `data/report_paperformat.xml`
- `report/hr_employee_certification_report_views.xml`
- `report/hr_employee_skill_history_report_views.xml`
- `report/hr_employee_skill_report_views.xml`
- `report/hr_employee_cv_report.xml`
- `views/hr_department_views.xml`
- `views/hr_employee_cv_templates.xml`
- `wizard/hr_employee_cv_wizard_views.xml`

## Demo
- `data/hr_skill_demo.xml`
- `data/hr_resume_demo.xml`
- `data/hr_job_skill_demo.xml`
- `data/hr.job.skill.csv`
- `data/hr.employee.skill.csv`
- `data/hr_employee_skill_demo.xml`
- `data/hr.resume.line.csv`

## Models
- `hr.employee` / `hr.employee.public`
- `hr.skill` / `hr.skill.level` / `hr.skill.type`
- `hr.employee.skill`
- `hr.job.skill`
- `hr.resume.line` / `hr.resume.line.type`
- `hr.department`
