# Module: payment_dpo
**Name:** Payment Provider: DPO
**Version:** (inherited from payment)
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'dpo'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `dpo_service_ref` | Char | Yes | DPO Service ID |
| `dpo_company_token` | Char | Yes | DPO company token |

## Default Payment Method Codes
`dpo`

## Security
No separate security file.

## Controllers
- `main.py`: Handles DPO payment processing and webhooks
