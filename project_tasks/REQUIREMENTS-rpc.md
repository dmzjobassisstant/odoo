# rpc — Requirements

## Module Overview
- **Name**: RPC endpoints
- **Version**: 1.0
- **Category**: Extra Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: Auto-install

## Dependencies
- `base`

## Core Functionality
Provides standard Odoo RPC endpoints (`/xmlrpc` and `/jsonrpc`) for programmatic access to Odoo models.

## Endpoints
- `/xmlrpc` — XML-RPC endpoint
- `/jsonrpc` — JSON-RPC endpoint

## Controllers
- `rpc/controllers/` directory contains RPC endpoint handlers

## Key Features
- Standard XML-RPC and JSON-RPC interface
- Model-agnostic access (any model can be accessed)
- Authentication via session

## Tests
- `rpc/tests/` contains unit tests for RPC functionality

## Security
- Standard Odoo authentication/authorization applies
