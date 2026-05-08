# Module: payment_adyen
**Name:** Payment Provider: Adyen
**Version:** 2.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'adyen'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `adyen_merchant_account` | Char | Yes | Adyen merchant account name |
| `adyen_api_key` | Char | Yes | Adyen API key |
| `adyen_client_key` | Char | Yes | Adyen client key |
| `adyen_hmac_key` | Char | Yes | Adyen HMAC key |
| `adyen_api_url_prefix` | Char | Yes | Adyen API URL prefix |

## Default Payment Method Codes
`card`, `visa`, `mastercard`, `amex`, `discover`

## Supported Currencies
All standard currencies; special decimals for: CLP, CVE, IDR, ISK (defined in const.py).

## Security
No separate security file; relies on base payment module security.

## Hooks
- `post_init_hook`: post-installation initialization
- `uninstall_hook`: cleanup on uninstall

## Controllers
- `main.py`: Handles Adyen payment processing, webhooks, cancel, capture, refund operations
