# Module: payment_xendit
**Name:** Payment Provider: Xendit
**Version:** 1.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'xendit'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `xendit_public_key` | Char | Yes | Xendit public key |
| `xendit_secret_key` | Char | Yes | Xendit secret key |
| `xendit_webhook_token` | Char | Yes | Xendit webhook token |

## Supported Currencies / Decimal Handling
IDR (0 decimals), MYR (0 decimals), PHP (0 decimals), THB (0 decimals), VND (0 decimals) — per CURRENCY_DECIMALS mapping.

## Default Payment Method Codes
**Primary:** `card`, `dana`, `ovo`, `qris`, `fpx`, `touch_n_go`, `promptpay`, `linepay`, `shopeepay`, `appota`, `zalopay`, `vnptwallet`
**Brand:** `visa`, `mastercard`

## FPX (Malaysia)
Supports both individual and business accounts for FPX payments.

## Security
No separate security file.

## Controllers
- `main.py`: Handles Xendit payment processing and webhooks
