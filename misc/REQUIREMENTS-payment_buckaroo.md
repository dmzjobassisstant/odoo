# Module: payment_buckaroo
**Name:** Payment Provider: Buckaroo
**Version:** 2.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'buckaroo'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `buckaroo_website_key` | Char | Yes | Buckaroo website key |
| `buckaroo_secret_key` | Char | Yes | Buckaroo secret key |

## Default Payment Method Codes
`card`, `visa`, `mastercard`, `amex`, `discover`

## Supported Payment Methods (via mapping)
alipay, apple_pay, bancontact, belfius, billink, cartes_bancaires, eps, giropay, in3, ideal, kbc, bank_reference, p24, paypal, poste_pay, sepa_direct_debit, sofort, tinka, trustly, wechat_pay, klarna, afterpay_riverty

## Security
No separate security file.

## Controllers
- `main.py`: Handles Buckaroo payment processing and webhooks
