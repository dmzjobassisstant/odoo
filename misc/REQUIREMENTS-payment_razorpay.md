# Module: payment_razorpay
**Name:** Payment Provider: Razorpay
**Version:** 1.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'razorpay'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `razorpay_key_id` | Char | No | Razorpay key ID |
| `razorpay_key_secret` | Char | No | Razorpay key secret |
| `razorpay_webhook_secret` | Char | No | Razorpay webhook secret |
| `razorpay_account_id` | Char | No | Razorpay account ID (OAuth) |
| `razorpay_refresh_token` | Char | No | OAuth refresh token |
| `razorpay_public_token` | Char | No | OAuth public token |
| `razorpay_access_token` | Char | No | OAuth access token |
| `razorpay_access_token_expiry` | Datetime | No | OAuth token expiry |

## Supported Currencies
AMD, ARS, AUD, AWG, BBD, BDT, BMD, BND, BOB, BSD, BWP, BZD, CAD, CHF, CNY, COP, CRC, CUP, CZK, DKK, DOP, DZD, EGP, ETB, EUR, FJD, GBP, GHS, GIP, GMD, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR (see const.py for full list)

## OAuth Support
Yes — supports OAuth tokens and refresh tokens.

## Security
No separate security file.

## Controllers
- `main.py`: Handles Razorpay payment processing and webhooks
- `onboarding.py`: OAuth onboarding flow
