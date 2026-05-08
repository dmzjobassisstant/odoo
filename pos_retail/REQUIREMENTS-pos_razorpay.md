# pos_razorpay

Manifest Name: POS Razorpay
Version: 1.0
Description: 
Allow Razorpay POS payments
==============================

This module allows customers to pay for their orders with debit/credit
cards and UPI. The transactions are processed by Razorpay POS. A Razorpay merchant account is necessary. It allows the
following:

* Fast payment by just swiping/scanning a credit/debit card or a QR code while on the payment screen
* Supported cards: Visa, MasterCard, Rupay, UPI
    
Summary: Integrate your POS with a Razorpay payment terminal

## Odoo Dependencies
- point_of_sale

## External Dependencies
None

## Models
- pos_payment.py
- pos_payment_method.py
- razorpay_pos_request.py
