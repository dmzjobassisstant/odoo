# Module: payment_aps
**Name:** Payment Provider: Amazon Payment Services
**Version:** 1.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'aps'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `aps_merchant_identifier` | Char | Yes | APS merchant identifier |
| `aps_access_code` | Char | Yes | APS access code |
| `aps_sha_request` | Char | Yes | SHA request phrase |
| `aps_sha_response` | Char | Yes | SHA response phrase |

## Default Payment Method Codes
`card`, `visa`, `mastercard`, `amex`, `discover`

## Security
No separate security file.

## Controllers
- `main.py`: Handles APS payment processing and webhooks
