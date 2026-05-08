# REQUIREMENTS — hr_presence (Employee Presence Control)

## Module Details
- **Name:** Employee Presence Control
- **Category:** Human Resources
- **Version:** 1.0
- **Author:** Odoo S.A.
- **License:** LGPL-3

## Depends
- `hr`
- `hr_holidays`
- `sms`

## Description
Control Employees Presence based on: IP Address, User's Session, Sent Emails. Allows contacting directly the employee in case of unjustified absence.

## Data Files
- `security/sms_security.xml`
- `security/ir.model.access.csv`
- `views/hr_employee_views.xml`
- `data/mail_template_data.xml`
- `data/sms_data.xml`
- `data/ir_cron.xml`

## Models
- `hr.employee`
- `sms.sms`
- `mail.mail`
