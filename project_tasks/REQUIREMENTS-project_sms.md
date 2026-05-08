# Project SMS Module Requirements

## Module Overview
- **Name**: Project - SMS
- **Version**: 1.1
- **Category**: Services/Project
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True

## Dependencies
- `project`
- `sms`

## Description
Send text messages when project/task stage moves.

## Models
- Extends `project.project` with SMS functionality
- Extends `project.task` with SMS functionality
- Extends `project.task.type` with SMS template
- Extends `project.stage` (mail.thread) with SMS

## Key Components
- SMS templates linked to stage changes
- Automatic SMS notification on stage transitions

## Views
- `project_stage_views.xml`
- `project_task_type_views.xml`
- `project_project_views.xml`
- `project_task_views.xml`

## Security
- `ir.model.access.csv` - SMS model access
- `project_sms_security.xml` - SMS-specific security rules