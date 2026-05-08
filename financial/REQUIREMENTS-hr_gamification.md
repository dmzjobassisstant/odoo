# REQUIREMENTS — hr_gamification (HR Gamification)

## Module Details
- **Name:** HR Gamification
- **Category:** Human Resources
- **Version:** 1.0
- **Author:** Odoo S.A.
- **License:** LGPL-3
- **Auto-install:** True

## Depends
- `gamification`
- `hr`

## Description
Use the HR resources for the gamification process. HR officer can manage challenges and badges. Allows sending badges to employees. Badge received are displayed on the user profile.

## Data Files
- `security/gamification_security.xml`
- `security/ir.model.access.csv`
- `wizard/gamification_badge_user_wizard_views.xml`
- `views/gamification_views.xml`
- `views/hr_employee_views.xml`

## Models
- `gamification.badge`
- `gamification.challenge`
- `gamification.badge.user`
- `hr.employee`
