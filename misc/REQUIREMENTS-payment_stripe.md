# Module: payment_stripe
**Name:** Payment Provider: Stripe
**Version:** 2.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'stripe'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `stripe_publishable_key` | Char | Yes | Stripe publishable key |
| `stripe_secret_key` | Char | Yes | Stripe secret key |
| `stripe_webhook_secret` | Char | No | Stripe webhook secret |

## Default Payment Method Codes
`card`, `bancontact`, `eps`, `ideal`, `p24`, `visa`, `mastercard`, `amex`, `discover`

## Supported Payment Methods (via mapping)
ach_direct_debit, bacs_direct_debit, becs_direct_debit, sepa_direct_debit, afterpay, clearpay, cash_app_pay, mobile_pay

## Indian Mandates Supported Currencies
USD, EUR, GBP, SGD, CAD, CHF, SEK, AED, JPY (see const.py)

## Proxy
Uses Stripe proxy: `https://stripe.api.odoo.com/api/stripe/`

## Security
No separate security file.

## Controllers
- `main.py`: Handles Stripe payment processing, webhooks, token operations
- `onboarding.py`: Stripe Connect onboarding
