# rating Requirements

## Module Overview
- **Name**: Customer Rating
- **Category**: Productivity
- **Description**: This module allows a customer to give rating.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.1
- **Installable**: True

## Technical Details

### Dependencies
- `mail`

### Data Files
- `views/rating_rating_views.xml`
- `views/rating_templates.xml`
- `views/mail_message_views.xml`
- `security/ir.model.access.csv`

### Assets
- `web.assets_backend`: Core common and web assets
- `web.assets_frontend`: Rating templates SCSS
- `web.assets_unit_tests`: Unit tests
- `mail.assets_public`: Public rating assets
- `portal.assets_chatter`: Chatter rating assets

### Models
- `rating.rating` - Rating records
- `rating.mixin` - Mixin for rating-enabled models
- `rating.parent.mixin` - Mixin for parent rating aggregation
- `mail.message` - Extended with rating references
