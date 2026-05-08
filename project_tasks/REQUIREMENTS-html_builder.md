# html_builder — Requirements

## Module Overview
- **Name**: HTML Builder
- **Version**: 0.1
- **Category**: Uncategorized
- **License**: LGPL-3
- **Author**: Odoo

## Dependencies
- `base`
- `html_editor`
- `mail`

## Core Functionality
Generic HTML builder application designed for use by website builder and mass mailing editor. Provides building blocks and snippets for HTML composition.

## Key Features
- Snippet system for HTML composition
- Background customization
- Iframe-based editing
- Mass mailing editor support
- Website builder integration

## Assets (Multiple Custom Bundles)

### `html_builder.assets`
- Primary variables SCSS
- Bootstrap + web variables
- Fonts, HTML builder source files
- Conditional removal of dark/editor styles

### `web.assets_frontend`
- Background SCSS

### `web.assets_web_dark`
- Dark mode SCSS files

### `html_builder.assets_inside_builder_iframe`
- Editor helpers, Bootstrap, ChatGPT plugin, link plugin SCSS

### `html_builder.iframe_add_dialog`
- Helpers, pre-variables, Bootstrap, snippet viewer SCSS

### `web.assets_unit_tests`
- HTML builder tests with included assets bundle

## Relationship to html_editor
- Depends on `html_editor` for the core editor component
- Extends it with builder-specific snippets and functionality
