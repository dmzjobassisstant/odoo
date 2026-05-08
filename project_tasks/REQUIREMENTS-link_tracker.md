# link_tracker — Requirements

## Module Overview
- **Name**: Link Tracker
- **Version**: 1.1
- **Category**: Marketing
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Installable

## Dependencies
- `utm`
- `mail`

## Core Functionality
Shortens URLs and tracks clicks and UTMs. Each tracked link records click counts and is associated with marketing campaigns.

## Key Models
- `link.tracker` — Link tracking (url, short_url, code, title, label, count, campaign_id, medium_id, source_id)
- `link.tracker.code` — Short URL codes
- `link.tracker.click` — Click records
- `utm.mixin` — Inherited for UTM tracking
- `mail.render.mixin` — For rendering tracked links in mail

## Key Features
- URL shortening with unique codes
- Click tracking per link
- UTM parameter integration (campaign, medium, source)
- Link label/button tracking
- Short URL code uniqueness across campaign/medium/source/label
- Link preview fetching

## Data Files
- `views/link_tracker_views.xml`
- `views/utm_campaign_views.xml`
- `security/ir.model.access.csv`

## Security
- Access control via `ir.model.access.csv`
