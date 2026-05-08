# Module: payment_custom
**Name:** Payment Provider: Custom Payment Modes
**Version:** 2.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'custom'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `custom_mode` | Selection | Yes | Mode: `wire_transfer` |
| `qr_code` | Boolean | No | Enable QR code generation |

## Default Payment Method Codes
`wire_transfer`

## Security
No separate security file.

## Controllers
- `main.py`: Handles custom payment processing
