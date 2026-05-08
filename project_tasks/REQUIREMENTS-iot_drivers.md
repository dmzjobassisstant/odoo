# iot_drivers — Requirements

## Module Overview
- **Name**: Hardware Proxy
- **Category**: Hidden
- **License**: LGPL-3
- **Author**: Odoo S.A.
- **Status**: NOT Installable

## Dependencies
None

## Core Functionality
Connects the Web Client to hardware peripherals. This module contains only the enabling framework — actual device drivers are in separate modules. Provides proxy services for printers, scales, displays, and other hardware.

## Key Components

### Core
- `main.py` — Main IoT drivers entry point
- `driver.py` — Base driver class
- `interface.py` — Hardware interfaces
- `event_manager.py` — Event management
- `connection_manager.py` — Connection management
- `browser.py` — Browser/hardware bridge
- `http.py` — HTTP endpoints for hardware
- `websocket_client.py` — WebSocket client
- `webrtc_client.py` — WebRTC client for audio/video
- `exception_logger.py` — Exception logging

### Tools
- `tools/wifi.py` — WiFi configuration
- `tools/upgrade.py` — Upgrade handling
- `tools/helpers.py` — Helper utilities
- `tools/system.py` — System utilities
- `tools/certificate.py` — Certificate management
- `tools/route.py` — Routing utilities

### Drivers
- `iot_handlers/drivers/serial_base_driver.py` — Base serial driver
- `iot_handlers/drivers/serial_scale_driver.py` — Scale driver
- `iot_handlers/drivers/printer_driver_base.py` — Base printer driver
- `iot_handlers/drivers/printer_driver_L.py` — Linux printer driver
- `iot_handlers/drivers/printer_driver_W.py` — Windows printer driver
- `iot_handlers/drivers/display_driver_L.py` — Linux display driver
- `iot_handlers/drivers/keyboard_usb_driver_L.py` — USB keyboard driver
- `iot_handlers/drivers/l10n_eg_drivers.py` — Egypt-specific drivers
- `iot_handlers/drivers/l10n_ke_edi_serial_driver.py` — Kenya EDI serial driver

### Interfaces
- `iot_handlers/interfaces/serial_interface.py` — Serial interface
- `iot_handlers/interfaces/printer_interface_L.py` — Linux printer interface
- `iot_handlers/interfaces/printer_interface_W.py` — Windows printer interface
- `iot_handlers/interfaces/display_interface_L.py` — Linux display interface
- `iot_handlers/interfaces/usb_interface_L.py` — USB interface (Linux)

### Controllers
- `controllers/homepage.py` — IoT homepage
- `controllers/proxy.py` — Proxy endpoints
- `controllers/driver.py` — Driver endpoints

### CLI
- `cli/genproxytoken.py` — Generate proxy token CLI

## Assets
- `iot_drivers.assets` bundle: All static files from `iot_drivers/static/**/*`

## Note
This module is not installable (`installable: False`). Device-specific drivers must be installed separately.
