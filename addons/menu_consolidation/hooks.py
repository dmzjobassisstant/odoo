import json
import logging

_logger = logging.getLogger(__name__)

# Menus whose parent_id this module overrides (see data/menu_groups.xml).
# Captured at install time so they can be restored on uninstall.
_REPARENTED_CHILDREN = [
    'hr.menu_hr_root',
    'hr_recruitment.menu_hr_recruitment_root',
    'hr_holidays.menu_hr_holidays_root',
    'hr_payroll_custom.menu_hr_payroll_root',
    'hr_issues.menu_hr_issues_root',
    'account.menu_finance',
    'sale.sale_menu_root',
    'hr_expense.menu_hr_expense_root',
    'timesheet_management.menu_timesheet_root',
    'project.menu_main_pm',
    'project_todo.menu_todo_todos',
    'purchase.menu_purchase_root',
    'supplier_management.menu_supplier_management_root',
    'contract_management.menu_contract_management_root',
    'board_reporting.menu_board_reporting_root',
    'competency_assessment.menu_competency_root',
    'spreadsheet_dashboard.spreadsheet_dashboard_menu_root',
    'calendar.mail_menu_calendar',
    'contacts.menu_contacts',
    'mail.menu_root_discuss',
    'document_templates.menu_document_layouts_root',
    'base.menu_administration',
    'utm.menu_link_tracker_root',
    'website.menu_website_configuration',
]

# Menus whose web_icon this module clears (hidden from the app drawer).
_HIDDEN_ICON_MENUS = [
    'base.menu_management',
    'base.menu_tests',
]


def pre_init_hook(env):
    """Capture the original parent_ids and web_icons of the menus this module
    will reparent/hide, BEFORE the reparenting data XML is applied.

    This runs before the module's data files are loaded, so the captured values
    reflect the true pre-installation state (most app root menus are top-level,
    i.e. parent_id = False).
    """
    params = env['ir.config_parameter'].sudo()
    parent_mapping = {}
    for child_ref in _REPARENTED_CHILDREN:
        menu = env.ref(child_ref, raise_if_not_found=False)
        if not menu:
            continue
        parent_xmlid = False
        if menu.parent_id:
            parent_xmlid = menu.parent_id.get_external_id().get(menu.parent_id.id)
        parent_mapping[child_ref] = parent_xmlid
    icon_mapping = {}
    for menu_ref in _HIDDEN_ICON_MENUS:
        menu = env.ref(menu_ref, raise_if_not_found=False)
        if menu:
            icon_mapping[menu_ref] = menu.web_icon or ''
    params.set_param('menu_consolidation.original_parents', json.dumps(parent_mapping))
    params.set_param('menu_consolidation.hidden_icons', json.dumps(icon_mapping))


def pre_uninstall_hook(env):
    """Restore the original parent_ids and web_icons before this module's
    group parent menus are cascade-deleted on uninstall.
    """
    params = env['ir.config_parameter'].sudo()
    original_map = params.get_param('menu_consolidation.original_parents')
    if original_map:
        try:
            mapping = json.loads(original_map)
        except (ValueError, TypeError):
            mapping = {}
        for child_ref, parent_ref in mapping.items():
            try:
                child = env.ref(child_ref, raise_if_not_found=False)
                if not child:
                    continue
                if parent_ref:
                    parent = env.ref(parent_ref, raise_if_not_found=False)
                    if parent:
                        child.sudo().parent_id = parent.id
                else:
                    # Restore to top-level (original state for app root menus)
                    child.sudo().parent_id = False
            except Exception as e:
                _logger.warning(
                    'menu_consolidation: failed to restore menu %s: %s',
                    child_ref, e,
                )
    hidden = params.get_param('menu_consolidation.hidden_icons')
    if hidden:
        try:
            icon_map = json.loads(hidden)
        except (ValueError, TypeError):
            icon_map = {}
        for ref, icon in icon_map.items():
            try:
                menu = env.ref(ref, raise_if_not_found=False)
                if menu:
                    menu.sudo().web_icon = icon or False
            except Exception as e:
                _logger.warning(
                    'menu_consolidation: failed to restore icon %s: %s',
                    ref, e,
                )
    # Clean up the config parameters
    params.set_param('menu_consolidation.original_parents', False)
    params.set_param('menu_consolidation.hidden_icons', False)
