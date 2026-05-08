# Project Module Requirements

## Module Overview
- **Name**: Project
- **Version**: 1.3
- **Category**: Services/Project
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Application**: Yes
- **Installable**: True

## Dependencies
- analytic
- base_setup
- mail
- portal
- rating
- resource
- web
- web_tour
- digest

## Description
Organize and plan your projects.

## Models
- `project.project` - Main project model with stages, milestones, tags, updates
- `project.task` - Task model with dependencies, recurrence, milestones, assignees
- `project.update` - Project status updates
- `project.task.type` - Task stages/types
- `project.project.stage` - Project stages
- `project.role` - Project roles for collaboration
- `project.milestone` - Project milestones
- `project.tags` - Task/project tags
- `project.collaborator` - Project collaborators
- `project.task.recurrence` - Task recurrence settings
- `account.analytic.account` - Analytic accounts for projects
- `res.partner` - Customer/partner integration
- `digest.digest` - Dashboard digest integration
- `mail.activity.plan` - Activity plans
- `mail.activity.type` - Activity types

## Key Features
- Project creation and management with stages
- Task management with subtasks, dependencies, recurrence
- Milestone tracking
- Project updates/status reporting
- Rating/feedback system
- Portal access for customers
- Project sharing with external users
- Favorite projects
- Task color coding and priorities
- Email alias integration
- Calendar view for tasks
- Burndown chart reporting
- Project templates

## Views
- Project kanban, list, form, calendar, activity views
- Task kanban, list, form, calendar, gantt, pivot, graph views
- Project update templates
- Portal templates for customer access
- Stage management views
- Tag management views

## Security
- `project_security.xml` - Project access rules
- `ir.model.access.csv` - Model access control
- `ir.model.access.xml` - Extended access control

## Assets (JavaScript/CSS)
- Backend assets: project.css, views, components, tours
- Frontend assets: portal rating SCSS, interactions
- Test assets: mock server, test models, tour tests
- Project webclient custom assets

## Hooks
- `post_init_hook`: `_project_post_init`
- `uninstall_hook`: `_project_uninstall_hook`

## Demo Data
- `mail_template_demo.xml`
- `project_demo.xml`