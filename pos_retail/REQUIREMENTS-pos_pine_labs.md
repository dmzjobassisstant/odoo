# pos_pine_labs

Manifest Name: POS Pine Labs
Version: 1.0
Description: 
Allow Pine Labs POS payments
==============================

This module is available only for companies that use INR currency.
It enables customers to pay for their orders using debit/credit cards and UPI through Pine Labs POS terminals.
A Pine Labs merchant account is required to process transactions.
Features include:

* Quick payments by swiping, scanning, or tapping your credit/debit card or UPI QR code at the payment terminal.
* Supported cards: Visa, MasterCard, RuPay.
    
Summary: Integrate your POS with Pine Labs payment terminals

## Odoo Dependencies
- point_of_sale

## External Dependencies
None

## Models
- pine_labs_pos_request.py
- pos_payment.py
- pos_payment_method.py
