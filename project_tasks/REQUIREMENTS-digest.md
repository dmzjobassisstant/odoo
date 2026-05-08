# Requirements: digest

## Module Overview
- **Name**: KPI Digests
- **Version**: 1.1
- **Category**: Marketing
- **Depends**: `mail`, `portal`, `resource`
- **License**: LGPL-3

## Description
Send KPI Digests periodically to users with tracked metrics.

## Dependencies

### Internal Dependencies
- `mail` - Mail/messaging module
- `portal` - Portal access for users
- `resource` - Resource planning module

## Models

### Core Models
| Model | Description |
|-------|-------------|
| `digest.digest` | Digest - KPI report configuration and sending |
| `digest.tip` | Digest Tip - contextual tips for users |
| `res.users` | Extended with digest preferences |
| `res.config.settings` | Extended with digest settings |

### Digest KPI Fields
- `kpi_res_users_connected` - Connected users metric
- `kpi_res_users_connected_value` - Connected users count
- `kpi_mail_message_total` - Messages sent metric
- `kpi_mail_message_total_value` - Messages count

## Views & Security

### Data Files
- `security/ir.model.access.csv` - Access control
- `data/digest_data.xml` - Digest KPI data
- `data/digest_tips_data.xml` - Tips data
- `data/ir_cron_data.xml` - Scheduled sending
- `data/res_config_settings_data.xml` - Config settings

### View Files
- `views/digest_views.xml`
- `views/digest_templates.xml`
- `views/res_config_settings_views.xml`

## Key Features
- Periodic KPI digest emails (daily, weekly, monthly, quarterly)
- Configurable KPI metrics
- User subscription management
- Unsubscribe tokens for users
- Digest slow-down based on user activity
- Customizable report templates
- Tips for improving metrics
- Company-based or global KPI computation
