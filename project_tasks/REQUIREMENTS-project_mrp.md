# Project MRP Module Requirements

## Module Overview
- **Name**: MRP Project
- **Version**: 1.0
- **Category**: Services/Project
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True

## Dependencies
- `mrp`
- `project`

## Description
Monitor MRP (Manufacturing) using project.

## Models
- Extends `project.project` with MRP-related fields and methods
- Extends `mrp.bom` (Bill of Materials) with project link
- Extends `mrp.production` with project link
- Extends `stock.move` (from MRP) with project link

## Key Fields (on project.project)
- `bom_count` - Count of Bills of Materials for the project
- `production_count` - Count of Manufacturing Orders for the project

## Key Methods
- `_compute_bom_count()` - Compute BOM count
- `_compute_production_count()` - Compute production count
- `action_view_mrp_bom()` - Action to view project's BOMs
- `action_view_mrp_production()` - Action to view project's manufacturing orders
- `_get_stat_buttons()` - Adds MRP stat buttons to project dashboard

## Views
- `mrp_bom_views.xml`
- `mrp_production_views.xml`
- `project_project_views.xml`