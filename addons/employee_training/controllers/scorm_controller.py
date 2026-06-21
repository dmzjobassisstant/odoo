import json
import logging
import os
import re

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class ScormController(http.Controller):

    @http.route('/training/scorm/<int:assignment_id>', type='http', auth='user', csrf=False)
    def scorm_launch(self, assignment_id, **kwargs):
        """Launch SCORM course for the given assignment."""
        assignment = request.env['training.assignment'].sudo().browse(assignment_id)
        if not assignment.exists():
            return request.not_found()

        course = assignment.course_id
        if course.course_type != 'scorm':
            return request.not_found()

        # Mark assignment as in progress
        if assignment.state == 'assigned':
            assignment.action_start()

        extract_dir = os.path.join('/tmp', 'scorm', str(course.id))
        entry_point = course.scorm_entry_point

        if not entry_point:
            return "No SCORM entry point configured for this course."

        entry_path = os.path.join(extract_dir, entry_point)
        if not os.path.exists(entry_path):
            return f"SCORM content not found: {entry_point}"

        content = open(entry_path, 'rb').read()
        content_str = content.decode('utf-8', errors='replace')

        # Inject SCORM Runtime API
        scorm_api = self._get_scorm_api_js(assignment)
        inject_html = f'<script>\n{scorm_api}\n</script>'
        content_str = content_str.replace('</head>', f'{inject_html}</head>', 1)
        if inject_html not in content_str:
            # If no head, inject at beginning
            content_str = inject_html + content_str

        return request.make_response(
            content_str,
            headers=[('Content-Type', 'text/html; charset=utf-8')]
        )

    @http.route('/training/scorm/api/<int:assignment_id>', type='jsonrpc', auth='user', csrf=False)
    def scorm_api(self, assignment_id, **kwargs):
        """SCORM API backend for LMSCommit, etc."""
        assignment = request.env['training.assignment'].sudo().browse(assignment_id)
        if not assignment.exists():
            return {'error': 'Assignment not found'}

        data = request.jsonrequest
        action = data.get('action')

        if action == 'commit':
            scorm_data = data.get('scorm_data', {})
            assignment.scorm_data = json.dumps(scorm_data)

            lesson_status = scorm_data.get('cmi.core.lesson_status', '')
            if lesson_status in ('completed', 'passed'):
                assignment.action_complete()

            # Update progress
            lesson_location = scorm_data.get('cmi.core.lesson_location', '')
            if lesson_location:
                try:
                    pct = float(lesson_location)
                    if 0 <= pct <= 100:
                        assignment.progress_pct = pct
                except (ValueError, TypeError):
                    pass

            score_raw = scorm_data.get('cmi.core.score.raw', '')
            if score_raw:
                try:
                    assignment.score = float(score_raw)
                except (ValueError, TypeError):
                    pass

            return {'status': 'ok'}

        return {'error': 'Unknown action'}

    def _get_scorm_api_js(self, assignment):
        """Generate the SCORM Runtime API JavaScript."""
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url', '')
        api_url = f'{base_url}/training/scorm/api/{assignment.id}'

        return f"""
// SCORM 1.2 Runtime API
var API_1484_11 = null;
var SCORM_API = null;

function findAPI(win) {{
    while (win.API_1484_11 == null && win.parent != null && win.parent != win) {{
        win = win.parent;
        findAPI(win);
    }}
    return win.API_1484_11;
}}

function getAPI() {{
    return findAPI(window);
}}

var _scormData = {{}};
var _apiUrl = '{api_url}';

function LMSInitialize(dummy) {{
    try {{
        var data = JSON.parse(document.getElementById('_scorm_stored_data')?.value || '{{}}');
        _scormData = data;
    }} catch(e) {{}}
    return 'true';
}}

function LMSFinish(dummy) {{
    LMSCommit('');
    try {{
        var xhr = new XMLHttpRequest();
        xhr.open('POST', _apiUrl, false);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({{action: 'finish', scorm_data: _scormData}}));
    }} catch(e) {{}}
    return 'true';
}}

function LMSGetValue(name) {{
    return _scormData[name] || '';
}}

function LMSSetValue(name, value) {{
    _scormData[name] = value;
    return 'true';
}}

function LMSCommit(dummy) {{
    try {{
        var xhr = new XMLHttpRequest();
        xhr.open('POST', _apiUrl, false);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({{action: 'commit', scorm_data: _scormData}}));
        var resp = JSON.parse(xhr.responseText);
    }} catch(e) {{
        // Silent fail for commit
    }}
    return 'true';
}}

function LMSGetLastError() {{ return '0'; }}
function LMSGetErrorString(err) {{ return ''; }}
function LMSGetDiagnostic(err) {{ return ''; }}

// Store data in hidden field on unload
window.addEventListener('beforeunload', function() {{
    var input = document.getElementById('_scorm_stored_data');
    if (!input) {{
        input = document.createElement('input');
        input.type = 'hidden';
        input.id = '_scorm_stored_data';
        document.body.appendChild(input);
    }}
    input.value = JSON.stringify(_scormData);
}});

API_1484_11 = {{
    LMSInitialize: LMSInitialize,
    LMSFinish: LMSFinish,
    LMSGetValue: LMSGetValue,
    LMSSetValue: LMSSetValue,
    LMSCommit: LMSCommit,
    LMSGetLastError: LMSGetLastError,
    LMSGetErrorString: LMSGetErrorString,
    LMSGetDiagnostic: LMSGetDiagnostic,
}};
"""
