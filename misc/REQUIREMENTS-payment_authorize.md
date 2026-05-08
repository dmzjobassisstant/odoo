# Module: payment_authorize
**Name:** Payment Provider: Authorize.Net
**Version:** 2.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'authorize'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `authorize_login` | Char | Yes | Authorize.Net API login ID |
| `authorize_transaction_key` | Char | Yes | Authorize.Net transaction key |
| `authorize_signature_key` | Char | Yes | Authorize.Net signature key |
| `authorize_client_key` | Char | No | Authorize.Net client key |

## Default Payment Method Codes
`ach_direct_debit`, `card`, `visa`, `mastercard`, `amex`, `discover`

## Feature Support
Authorize.Net supports only one currency per gateway account. Tokenization is supported.

## Security
No separate security file.

## Controllers
- `main.py`: Handles Authorize.Net payment processing, webhooks, ACH, token operations
