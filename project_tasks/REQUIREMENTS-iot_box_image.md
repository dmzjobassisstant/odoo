# iot_box_image — Requirements

## Module Overview
- **Name**: IoT Box Image Build Tools
- **Version**: 1.0
- **Category**: Hidden/Tools
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: NOT Installable

## Dependencies
None

## Core Functionality
Build tools for creating the IoT Box image. Contains scripts and configuration for building the Raspberry Pi / IoT Box OS image.

## Key Components
- `build_image.sh` — Main image build script
- `build_utils` — Build utility scripts
- `configuration/` — Image configuration files
- `overwrite_after_init/` — Files to add after init
- `overwrite_before_init/` — Files to add before init

## Note
This module is not installable (`installable: False`). It is used for building IoT Box images during the OS build process, not for runtime use in an Odoo database.
