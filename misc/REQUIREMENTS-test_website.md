# Requirements - test_website

**Module:** Website Test  
**Version:** 1.0  
**Category:** Hidden  
**License:** LGPL-3  
**Author:** Odoo S.A.

## Description
This module contains tests related to website. Those are present in a separate module as we are testing module install/uninstall/upgrade and we don't want to reload the website module every time, including it's possible dependencies. Neither we want to add in website module some routes, views and models which only purpose is to run tests.

## Dependencies
- web_unsplash
- website
- theme_default

## Demo Data
- data/test_website_demo.xml

## Data Files
- security/test_website_security.xml
- security/ir.model.access.csv
- views/templates.xml
- views/test_model_multi_website_views.xml
- views/test_model_views.xml
- data/test_website_data.xml

## Assets
- test_website.test_bundle: External JS/CSS links
- web.assets_frontend: test_website/static/src/interactions/**/*
- web.assets_tests: test_website/static/tests/tours/*