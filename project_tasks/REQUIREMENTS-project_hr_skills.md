# Project HR Skills Module Requirements

## Module Overview
- **Name**: Project - Skills
- **Version**: 1.0
- **Category**: Services/Project
- **Author**: Odoo S.A.
- **License**: OEEL-1
- **Auto-install**: True

## Dependencies
- `project`
- `hr_skills`

## Description
Search project tasks according to the assignees' skills.

## Models
- Extends `project.task` with skill-related fields

## Key Fields
- `user_skill_ids` - One2many to `hr.employee.skill`, related from `user_ids.employee_skill_ids`

## Views
- `project_task_views.xml` - Adds skill filtering/search capability to tasks