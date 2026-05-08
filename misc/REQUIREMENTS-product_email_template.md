---
name: product_email_template
summary: Add email templates to products to be sent on invoice confirmation
description: Add email templates to products to be sent on invoice confirmation. With this module, link your products to a template to send complete information and tools to your customer. For instance when invoicing a training, the training agenda and materials will automatically be sent to your customers.
author: Odoo S.A.
version: '1.0'
depends: account
external_dependencies: []
data_entities:
  - mail.template: Email template linked to product
    fields: [name, model_id, subject, body_html]
  - product.template: Product with email template
    fields: [name, product_email_template_id]
views:
  - xml: product_views.xml - Product Views
  - xml: mail_template_views.xml - Mail Template Views
access_rights:
  - base.user: read,write
business_logic:
  - _send_product_email: Send email template on invoice confirmation
  - action_send_email_template: Manual send of product email
external_integrations:
  - mail: Send product information emails on invoicing
---