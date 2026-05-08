# Module: payment_worldline
**Name:** Payment Provider: Worldline
**Version:** (inherited from payment)
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'worldline'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `worldline_pspid` | Char | Yes | Worldline PSP ID |
| `worldline_api_key` | Char | Yes | Worldline API key |
| `worldline_api_secret` | Char | Yes | Worldline API secret |
| `worldline_webhook_key` | Char | Yes | Worldline webhook key |
| `worldline_webhook_secret` | Char | Yes | Worldline webhook secret |

## Default Payment Method Codes
`card`, `visa`

## Supported Payment Methods (via mapping)
alipay_plus, amex, bancontact, bizum, cartes_bancaires, cofidis, diners, discover, eps, floa_bank, ideal, jcb, klarna, maestro, mastercard, mbway, multibanco, p24, paypal, post_finance_pay, twint, upi, visa, wechat_pay

## Redirect Payment Methods
alipay_plus, bizum, eps, floa_bank, ideal, klarna, mbway, multibanco, p24, paypal, post_finance_pay, twint, wechat_pay

## Security
No separate security file.

## Controllers
- `main.py`: Handles Worldline payment processing and webhooks
