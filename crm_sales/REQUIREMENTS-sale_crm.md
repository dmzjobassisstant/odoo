# Opportunity to Quotation (sale_crm)

## Module Details

- **Name**: Opportunity to Quotation
- **Version**: 1.0
- **Category**: Sales/Sales
- **Summary**: Shortcut on opportunity cases to generate sales orders
- **Description**: This module adds a shortcut on one or several opportunity cases in the CRM to generate a sales order based on the selected case. If different cases are open, it generates one sales order per case. The case is then closed and linked to the generated sales order.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Auto Install**: True

## Dependencies

| Type | Module |
|------|--------|
| Core | sale |
| Core | crm |

## External Dependencies

None

## Security

- `security/ir.model.access.csv`

## Data Files

- `data/crm_lead_merge_template.xml`
- `views/sale_order_views.xml`
- `views/crm_lead_views.xml`
- `views/crm_team_views.xml`
- `wizard/crm_opportunity_to_quotation_views.xml`

## Models

- `crm_lead.py`
- `crm_team.py`
- `sale_order.py`

## Hooks

- Uninstall hook: `uninstall_hook`
