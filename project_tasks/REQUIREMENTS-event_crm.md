# Requirements: event_crm

## Module Overview
- **Name**: Event CRM
- **Version**: 1.0
- **Category**: Marketing/Events
- **Website**: https://www.odoo.com/app/events
- **Depends**: `event`, `crm`
- **Auto-install**: Yes
- **License**: LGPL-3

## Description
Create leads from event registrations.

## Dependencies

### Internal Dependencies
- `event` - Event module
- `crm` - CRM module

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `event.lead.rule` | Lead Generation Rule - triggers on registration |
| `event.lead.request` | Lead Request - batch lead creation |
| `event.registration` | Extended with lead linking |
| `crm.lead` | Extended with event fields |
| `event.question.answer` | Extended for lead tracking |

### Event Registration Extensions
- `lead_ids` - Many2many to CRM leads
- `lead_count` - Computed lead count
- Lead generation on create/confirm/done triggers

## Views & Security

### Data Files
- `security/event_crm_security.xml` - CRM security rules
- `security/ir.model.access.csv` - Access control
- `data/crm_lead_merge_template.xml` - Lead merge templates
- `data/ir_action_data.xml` - Action definitions
- `data/ir_cron_data.xml` - Scheduled actions

### View Files
- `views/crm_lead_views.xml`
- `views/event_registration_views.xml`
- `views/event_lead_rule_views.xml`
- `views/event_event_views.xml`
- `views/event_question_views.xml`

## Key Features
- Automatic lead creation from event registrations
- Lead generation rules (trigger on create/confirm/done)
- Lead contact info from registration
- Lead description from registration answers
- UTM tracking integration (campaign, source, medium)
- Lead type (lead/opportunity)
- Sales team and user assignment from rules
- Tag assignment from rules
