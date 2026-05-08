# Requirements: base_sparse_field

## Module Details

- **Name**: Sparse Fields
- **Category**: Hidden
- **Version**: 1.0
- **License**: LGPL-3
- **Author**: Odoo S.A.

## Dependencies

- base

## Data Files

- security/ir.model.access.csv
- views/views.xml

## External Dependencies

None

## Description

Implementation of sparse fields. The purpose is to implement "sparse" fields, i.e., fields that are mostly null. This implementation circumvents the PostgreSQL limitation on the number of columns in a table. The values of all sparse fields are stored in a "serialized" field in the form of a JSON mapping.
