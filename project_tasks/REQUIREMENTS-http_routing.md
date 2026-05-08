# http_routing — Requirements

## Module Overview
- **Name**: Web Routing
- **Version**: 1.0
- **Category**: Hidden
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Installable

## Dependencies
- `web`

## Core Functionality
Provides advanced routing options beyond basic web or base routing. Implements custom URL slugging, model converters, and geo-ip routing.

## Key Models
- `ir.http` — Extended with advanced routing
- `ir.qweb` — QWeb rendering extended for routing
- `res.lang` — Extended for language routing

## Key Features
- Custom slug pattern (`_UNSLUG_RE`) with support for multi-word slugs
- `ModelConverter` — Enhanced model URL converter supporting negative IDs
- `_slug()` / `_unslug()` — URL slug handling
- `_unslug_url()` — Convert slugs back to record URLs
- Rerouting support with limit
- Geo-IP based routing (country/lang redirect)
- SEO-friendly URLs

## Data Files
- `views/http_routing_template.xml`
- `views/res_lang_views.xml`

## Hooks
- `_post_init_hook` — Post-install initialization

## External Dependencies
- `werkzeug` — URL parsing, routing, exceptions
- `urllib.parse` — URL parsing
- `pytz` — Timezone (via Odoo)

## Security
- Standard Odoo controller authentication
