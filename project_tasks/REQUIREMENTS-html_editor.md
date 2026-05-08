# html_editor — Requirements

## Module Overview
- **Name**: HTML Editor
- **Version**: 1.0
- **Category**: Hidden
- **License**: LGPL-3
- **Author**: Odoo

## Dependencies
- `base`
- `bus`
- `web`

## Core Functionality
Provides an extensible HTML editor component and plugin system. Used by website builder, mass mailing, and other modules requiring rich text editing.

## Key Models
- `ir.attachment` — Extended for HTML editor
- `ir.http` — Extended for editor routing
- `ir.qweb.fields` — QWeb field handlers
- `ir.ui.view` — Extended for editor
- `ir.websocket` — WebSocket for real-time
- `html_field.history.mixin` — History tracking for HTML fields
- `diff_utils` — Diff utilities

## Key Features
- Plugin-based architecture
- Media dialog (images, files)
- Collaboration support
- History tracking
- Image cropper (cropperjs, webgl-image-filter)
- Code highlighting (PrismJS)
- Dark mode support
- Local overlay for embedded content

## Data Files
- `security/ir.model.access.csv`

## Assets (Multiple Custom Bundles)

### `html_editor.assets_editor`
- DOMPurify, media dialog, history, core, main plugins, collaboration, embedded components, QWeb picker/plugin

### `html_editor.assets_history_diff`
- diff2html CSS/JS

### `html_editor.assets_media_dialog`
- Switch component, media dialog

### `html_editor.assets_readonly`
- HTML viewer, local overlay, list, file styles, embedded utils

### `html_editor.assets_image_cropper`
- CropperJS CSS/JS, webgl-image-filter

### `html_editor.assets_prism` / `assets_prism_dark`
- PrismJS with default/okaida themes

### `web.report_assets_common`
- Base styles for reports

## SCSS Overrides
- `primary_variables.scss` — After web primary variables
- `secondary_variables.scss` — Secondary variables
- `bootstrap_overridden.scss` / `bootstrap_overridden_backend.scss` / `bootstrap_overridden_frontend.scss`
- `html_editor.common.scss` / `html_editor.backend.scss` / `html_editor.frontend.scss`

## Security
- Access control via `ir.model.access.csv`
