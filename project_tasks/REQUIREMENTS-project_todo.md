# Project Todo Module Requirements

## Module Overview
- **Name**: To-Do
- **Version**: 1.0
- **Category**: Productivity/To-Do
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Application**: True
- **Installable**: True

## Dependencies
- `project`

## Description
Organize your work with memos and to-do lists. A lightweight task management app.

## Models
- Extends `project.task` with todo-specific functionality

## Key Methods
- `create()` - Auto-generate name from description if not provided
- `action_convert_to_task()` - Convert todo to full project task
- `get_todo_views_id()` - Returns available todo view IDs (kanban, list, form, calendar, activity)

## Key Features
- Simple to-do items derived from project tasks
- Quick creation from description
- Convert to full tasks
- Dedicated todo-specific views

## Security
- `ir.model.access.csv` - Model access control
- `project_todo_security.xml` - Todo-specific security rules

## Hooks
- `_todo_post_init` - Post-initialization hook

## Views
- `project_task_views.xml`
- `project_todo_menus.xml`
- `mail_activity_todo_create.xml` (wizard)

## Assets
- Backend: components, SCSS (todo.scss), views, web assets
- Tests: tour tests, unit tests

## Demo Data
- `todo_template.xml`