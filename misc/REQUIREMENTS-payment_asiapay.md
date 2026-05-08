# Module: payment_asiapay
**Name:** Payment Provider: AsiaPay
**Version:** 1.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'asiapay'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `asiapay_brand` | Selection | Yes | Brand: `paydollar`, `pesopay`, `siampay` |
| `asiapay_merchant_id` | Char | Yes | AsiaPay merchant ID |
| `asiapay_secure_hash_secret` | Char | Yes | Secure hash secret |
| `asiapay_secure_hash_function` | Selection | Yes | Hash function: `sha1`, `sha256`, `sha512` |

## Supported Currencies
AED, AUD, BND, CAD, CNY, EUR, GBP, HKD, IDR, INR, JPY, KRW, MOP, MYR, NZD, PHP, SAR, SGD, THB, TWD, USD, VND (mapped via CURRENCY_MAPPING)

## Security
No separate security file.

## Controllers
- `main.py`: Handles AsiaPay payment processing and webhooks
