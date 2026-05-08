# Project Mail Plugin Module Requirements

## Module Overview
- **Name**: Project Mail Plugin
- **Version**: 1.0
- **Category**: Services/Project
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True
- **Installable**: True

## Dependencies
- `project`
- `mail_plugin`

## Description
Integrate your inbox with projects. Turn emails received in your mailbox into tasks and log their content as internal notes.

## Structure
- `__manifest__.py`
- `controllers/` - Mail plugin controllers
- `views/` - Project task views with mail plugin integration
- `static/` - Static assets
- `tests/` - Test files
- `i18n/` - Internationalization

## Views
- `project_task_views.xml` - Task views with mail plugin integration