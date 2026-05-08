# Project Purchase Module Requirements

## Module Overview
- **Name**: Project Purchase
- **Version**: 1.0
- **Category**: Services/Project
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto-install**: True

## Dependencies
- `purchase`
- `project_account`

## Description
Monitor purchase in project. Adds purchase orders section to project profitability.

## Models
- Extends `project.project` with purchase-related fields and methods
- Extends `purchase.order` with project link
- Extends `purchase.order.line` with analytic distribution

## Key Fields (on project.project)
- `purchase_orders_count` - Count of purchase orders related to project

## Key Methods
- `_compute_purchase_orders_count()` - Compute purchase orders count
- `action_open_project_purchase_orders()` - Open project's purchase orders
- `action_profitability_items()` - Handle 'purchase_order' section
- `_get_stat_buttons()` - Adds purchase stat button
- `_get_profitability_aal_domain()` - Exclude purchase line move lines
- `_add_purchase_items()` - Disabled (purchase items handled separately)
- `_get_profitability_labels()` - Adds 'Purchase Orders' label
- `_get_profitability_sequence_per_invoice_type()` - Sequence for purchase (10)
- `_get_profitability_items()` - Gets purchase order profitability

## Views
- `project_project.xml`
- `purchase_order.xml`

## Assets
- `project_purchase/static/src/product_catalog/kanban_record.js`

## Demo Data
- `project_purchase_demo.xml`