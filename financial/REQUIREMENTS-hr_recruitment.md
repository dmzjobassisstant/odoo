# REQUIREMENTS — hr_recruitment (Recruitment)

## Module Details
- **Name:** Recruitment
- **Category:** Human Resources/Recruitment
- **Version:** 1.1
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Application:** Yes

## Depends
- `hr`
- `calendar`
- `utm`
- `attachment_indexation`
- `web_tour`
- `digest`

## Description
Track your recruitment pipeline.

## Data Files
- `security/hr_recruitment_security.xml`
- `security/ir.model.access.csv`
- `data/digest_data.xml`
- `data/mail_message_subtype_data.xml`
- `data/mail_template_data.xml`
- `data/mail_templates.xml`
- `data/hr_recruitment_data.xml`
- `data/hr_recruitment_tour.xml`
- `views/hr_recruitment_degree_views.xml`
- `views/hr_recruitment_source_views.xml`
- `views/hr_recruitment_stage_views.xml`
- `views/ir_attachment_views.xml`
- `views/hr_applicant_category_views.xml`
- `views/hr_applicant_refuse_reason_views.xml`
- `views/hr_applicant_views.xml`
- `views/hr_talent_pool_views.xml`
- `views/res_config_settings_views.xml`
- `views/hr_department_views.xml`
- `views/hr_job_views.xml`
- `views/mail_activity_views.xml`
- `views/mail_activity_plan_views.xml`
- `views/digest_views.xml`
- `wizard/applicant_refuse_reason_views.xml`
- `wizard/applicant_send_mail_views.xml`
- `wizard/talent_pool_add_applicants_views.xml`
- `wizard/job_add_applicants_views.xml`
- `views/menuitems.xml`

## Demo
- `data/hr_recruitment_demo.xml`

## Models
- `hr.applicant`
- `hr.applicant.category`
- `hr.applicant.refuse.reason`
- `hr.recruitment.degree`
- `hr.recruitment.source`
- `hr.recruitment.stage`
- `hr.talent.pool`
- `hr.job`
- `hr.department`
- `ir.attachment`
- `calendar.event`
- `mail.activity` / `mail.activity.plan`
- `utm.source` / `utm.medium` / `utm.campaign`
