# resource Requirements

## Module Overview
- **Name**: Resource
- **Category**: Hidden
- **Description**: Module for resource management. A resource represents something that can be scheduled (a developer on a task or a work center on manufacturing orders). Manages resource calendars and leaves.
- **Author**: Odoo S.A.
- **License**: LGPL-3
- **Version**: 1.1

## Technical Details

### Dependencies
- `base`
- `web`

### Data Files
- `data/resource_data.xml`
- `security/ir.model.access.csv`
- `security/resource_security.xml`
- `views/resource_resource_views.xml`
- `views/resource_calendar_leaves_views.xml`
- `views/resource_calendar_attendance_views.xml`
- `views/resource_calendar_views.xml`
- `views/menuitems.xml`

### Demo Data
- `data/resource_demo.xml`

### Assets
- `web.assets_backend`: All static src files
- `web.assets_unit_tests`: Unit tests

### Models
- `resource.resource` - Resource model (calendar-attached)
- `resource.calendar` - Working time calendars
- `resource.calendar.attendance` - Working hours
- `resource.calendar.leaves` - Resource leaves/absences
