# Requirements: bus

## Module Details

- **Name**: IM Bus
- **Category**: Hidden
- **Version**: 1.0
- **License**: LGPL-3
- **Author**: Odoo S.A.

## Dependencies

- base
- web

## Data Files

- security/ir.model.access.csv

## External Dependencies

None

## Assets

- web.assets_backend: 
  - bus/static/src/*.js
  - bus/static/src/debug/**/*
  - bus/static/src/services/**/*.js
  - bus/static/src/workers/*
- web.assets_frontend:
  - bus/static/src/*.js
  - bus/static/src/services/**/*.js
  - bus/static/src/workers/*
- web.assets_unit_tests: bus/static/tests/**/*
- bus.websocket_worker_assets:
  - web/static/src/module_loader.js
  - bus/static/src/workers/*

## Auto Install

- True

## Installable

- True

## Description

Instant Messaging Bus that allows sending messages to users in live.
