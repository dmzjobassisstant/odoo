# Module: payment_flutterwave
**Name:** Payment Provider: Flutterwave
**Version:** 1.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'flutterwave'`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `flutterwave_public_key` | Char | Yes | Flutterwave public key |
| `flutterwave_secret_key` | Char | Yes | Flutterwave secret key |
| `flutterwave_webhook_secret` | Char | Yes | Flutterwave webhook secret |

## Default Payment Method Codes
`card`, `mpesa`, `visa`, `mastercard`, `amex`, `discover`

## Supported Currencies
CLP, COP, EGP, EUR, GHS, GNF, KES, MWK, MAD, NGN, RWF, SLL, STD, ZAR, TZS, UGX, USD, XOF, ZMW

## Security
No separate security file.

## Controllers
- `main.py`: Handles Flutterwave payment processing and webhooks
