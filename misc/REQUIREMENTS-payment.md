# Module: payment
**Name:** Payment Engine
**Version:** 2.0
**Category:** Hidden
**License:** LGPL-3

## Dependencies
- `onboarding`
- `portal`

## Description
The payment engine used by payment provider modules.

## External Dependencies
None

## Key Models

### payment.provider
Base provider configuration fields:
- `name` (Char, required): Provider display name
- `code` (Selection): Provider code (`none` default)
- `state` (Selection): `disabled`, `enabled`, `test` — default: `disabled`
- `is_published` (Boolean)
- `company_id` (Many2one, required): `res.company`
- `main_currency_id` (Many2one, related to `company_id.currency_id`)
- `payment_method_ids` (Many2many): `payment.method`
- `allow_tokenization` (Boolean)
- `capture_manually` (Boolean)
- `allow_express_checkout` (Boolean)
- `redirect_form_view_id` (Many2one): `ir.ui.view`
- `inline_form_view_id` (Many2one): `ir.ui.view`
- `token_inline_form_view_id` (Many2one): `ir.ui.view`
- `express_checkout_form_view_id` (Many2one): `ir.ui.view`
- `available_country_ids` (Many2many): `res.country`
- `available_currency_ids` (Many2many): `res.currency`
- `maximum_amount` (Monetary)
- `pre_msg`, `pending_msg`, `auth_msg`, `done_msg`, `cancel_msg` (Html)
- `support_tokenization` (Boolean)
- `support_manual_capture` (Selection)
- `support_express_checkout` (Boolean)
- `support_refund` (Selection)
- `color` (Integer)
- `module_id` (Many2one): `ir.module.module`
- `module_state` (Selection, related)
- `module_to_buy` (Boolean, related)

### payment.transaction
- `provider_id` (Many2one): `payment.provider`
- `provider_code` (Selection, related)
- `company_id` (Many2one): `res.company`
- `payment_method_id` (Many2one): `payment.method`
- `payment_method_code` (Char)
- `primary_payment_method_id` (Many2one)
- `reference` (Char)
- `provider_reference` (Char)
- `amount` (Monetary)
- `currency_id` (Many2one): `res.currency`
- `token_id` (Many2one): `payment.token`
- `state` (Selection)
- `state_message` (Text)
- `last_state_change` (Datetime)
- `operation` (Selection)
- `is_live` (Boolean)
- `source_transaction_id` (Many2one)
- `child_transaction_ids` (One2many)
- `refunds_count` (Integer, computed)
- `is_post_processed` (Boolean)
- `tokenize` (Boolean)
- `landing_route` (Char)
- `partner_id` (Many2one): `res.partner`
- `partner_name`, `partner_lang`, `partner_email`, `partner_address`, `partner_zip`, `partner_city` (Char)
- `partner_state_id`, `partner_country_id` (Many2one)
- `partner_phone` (Char)

### payment.method
- `name` (Char, required, translate)
- `code` (Char)
- `sequence` (Integer, default: 1)
- `primary_payment_method_id` (Many2one)
- `brand_ids` (One2many)
- `is_primary` (Boolean)
- `provider_ids` (Many2many): `payment.provider`
- `active` (Boolean, default: True)
- `image` (Image)
- `image_payment_form` (Image)
- `support_tokenization` (Boolean)
- `support_express_checkout` (Boolean)
- `support_manual_capture` (Selection)
- `support_refund` (Selection)
- `supported_country_ids` (Many2many): `res.country`
- `supported_currency_ids` (Many2many): `res.currency`

### payment.token
- `provider_id` (Many2one, required): `payment.provider`
- `provider_code` (Selection, related)
- `company_id` (Many2one)
- `payment_method_id` (Many2one)
- `payment_method_code` (Char)
- `payment_details` (Char)
- `partner_id` (Many2one, required): `res.partner`
- `provider_ref` (Char)
- `transaction_ids` (One2many)
- `active` (Boolean, default: True)

## Security
- `ir.model.access.csv`
- `paymentSecurity.xml`

## Views / Assets
- QWeb templates: `express_checkout_templates.xml`, `payment_form_templates.xml`, `portal_templates.xml`
- Model views: `payment_provider_views.xml`, `payment_method_views.xml`, `payment_transaction_views.xml`, `payment_token_views.xml`, `res_partner_views.xml`
- Wizard views: `payment_capture_wizard_views.xml`, `payment_link_wizard_views.xml`
- Assets: JS (`payment/static/src/**/*`), SCSS (`payment/static/src/scss/payment_provider.scss`)
