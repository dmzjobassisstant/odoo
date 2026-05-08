# utm Requirements

## Module Overview
- **Name**: UTM Trackers
- **Category**: Marketing
- **Description**: Enable management of UTM trackers: campaign, medium, source.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.1

## Technical Details

### Dependencies
- `base`
- `web`
- Installable: True

### Data Files
- `data/utm_medium_data.xml`
- `data/utm_source_data.xml`
- `data/utm_stage_data.xml`
- `data/utm_tag_data.xml`
- `views/utm_campaign_views.xml`
- `views/utm_medium_views.xml`
- `views/utm_source_views.xml`
- `views/utm_stage_views.xml`
- `views/utm_tag_views.xml`
- `views/utm_menus.xml`
- `security/ir.model.access.csv`

### Demo Data
- `data/utm_campaign_demo.xml`
- `data/utm_stage_demo.xml`

### Assets
- `web.assets_backend`: All static src files

### Models
- `utm.campaign` - Marketing campaigns (UTM tracking)
- `utm.medium` - Marketing mediums (email, social, etc.)
- `utm.source` - Marketing sources (google, facebook, etc.)
- `utm.tag` - Tags for campaign organization
- `utm.stage` - Campaign stages

### Purpose
Tracks marketing sources and campaigns using UTM parameters. Records where leads/opportunities come from.
