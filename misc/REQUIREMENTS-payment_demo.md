# Module: payment_demo
**Name:** Payment Provider: Demo
**Version:** 2.0
**Category:** Accounting/Payment Providers
**License:** LGPL-3

## Dependencies
- `payment`

## External Dependencies
None

## Provider Configuration Fields
Inherits from `payment.provider`; adds `code = 'demo'`. No additional fields required.

## Default Payment Method Codes
`demo`

## Feature Support
Supports tokenization, manual capture, express checkout, refunds (via parent class computation).

## Security
No separate security file.

## Controllers
- `main.py`: Handles demo payment processing (for testing purposes)
