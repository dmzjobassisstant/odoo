import base64
import io
import json
import logging
import os
import zipfile
import xml.etree.ElementTree as ET

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Training Course'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence, name'

    name = fields.Char(required=True, tracking=True)
    description = fields.Html()
    course_type = fields.Selection(
        [('scorm', 'SCORM'),
         ('video', 'Video'),
         ('document', 'Document'),
         ('quiz', 'Quiz')],
        string='Course Type',
        required=True,
        default='document',
        tracking=True,
    )
    scorm_package = fields.Binary(
        string='SCORM Package',
        attachment=True,
    )
    scorm_package_filename = fields.Char(string='SCORM Package Filename')
    scorm_entry_point = fields.Char(string='SCORM Entry Point')
    duration_hours = fields.Float(string='Duration (Hours)')
    plan_id = fields.Many2one('training.plan', string='Training Plan')
    active = fields.Boolean(default=True, tracking=True)
    sequence = fields.Integer(default=10)

    @api.model
    def _extract_scorm_package(self, scorm_data, course_id):
        """Extract SCORM zip and find entry point from imsmanifest.xml."""
        extract_dir = os.path.join('/tmp', 'scorm', str(course_id))
        if os.path.exists(extract_dir):
            import shutil
            shutil.rmtree(extract_dir)
        os.makedirs(extract_dir, exist_ok=True)

        zip_bytes = base64.b64decode(scorm_data)
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
            # Prevent Zip Slip: verify each member path stays within extract_dir
            extract_abs = os.path.abspath(extract_dir)
            for member in zf.infolist():
                member_path = os.path.abspath(os.path.join(extract_dir, member.filename))
                if not member_path.startswith(extract_abs + os.sep):
                    _logger.warning('Skipping unsafe path in SCORM zip: %s', member.filename)
                    continue
                zf.extract(member, extract_dir)

        # Find imsmanifest.xml
        manifest_path = None
        for root, dirs, files in os.walk(extract_dir):
            for f in files:
                if f.lower() == 'imsmanifest.xml':
                    manifest_path = os.path.join(root, f)
                    break
            if manifest_path:
                break

        if not manifest_path:
            _logger.warning('No imsmanifest.xml found in SCORM package for course %s', course_id)
            return None

        try:
            tree = ET.parse(manifest_path)
            root_el = tree.getroot()
            # Default namespace for SCORM manifests
            ns = {'adlcp': 'http://www.adlnet.org/xsd/adlcp_rootv1p2',
                  'imscp': 'http://www.imsproject.org/xsd/imscp_rootv1p1p2'}
            # Try to find resource href
            # First try with namespace
            resources = root_el.findall('.//imscp:resources/imscp:resource', ns)
            if not resources:
                resources = root_el.findall('.//{http://www.imsproject.org/xsd/imscp_rootv1p1p2}resources/{http://www.imsproject.org/xsd/imscp_rootv1p1p2}resource')
            if not resources:
                # Fallback: strip namespaces
                for elem in root_el.iter():
                    elem.tag = elem.tag.split('}', 1)[-1] if '}' in elem.tag else elem.tag
                resources = root_el.findall('.//resources/resource')

            if resources:
                href = resources[0].get('href')
                if href:
                    # Make path relative to manifest
                    manifest_dir = os.path.dirname(manifest_path)
                    entry_full = os.path.join(manifest_dir, href)
                    entry_rel = os.path.relpath(entry_full, extract_dir)
                    return entry_rel
        except Exception as e:
            _logger.warning('Error parsing imsmanifest.xml: %s', e)

        # Fallback: look for index.html, index.htm, or any .html
        for root, dirs, files in os.walk(extract_dir):
            for f in files:
                if f.lower() in ('index.html', 'index.htm'):
                    return os.path.relpath(os.path.join(root, f), extract_dir)
            for f in files:
                if f.lower().endswith('.html') or f.lower().endswith('.htm'):
                    return os.path.relpath(os.path.join(root, f), extract_dir)

        return None

    @api.model_create_multi
    def create(self, vals_list):
        courses = super().create(vals_list)
        for course in courses:
            if course.scorm_package and course.course_type == 'scorm':
                entry_point = course._extract_scorm_package(
                    course.scorm_package, course.id
                )
                if entry_point:
                    super(TrainingCourse, course).write({
                        'scorm_entry_point': entry_point,
                    })
        return courses

    def write(self, vals):
        res = super().write(vals)
        if vals.get('scorm_package') and self.course_type == 'scorm':
            for course in self:
                entry_point = self._extract_scorm_package(
                    vals['scorm_package'], course.id
                )
                if entry_point:
                    super(TrainingCourse, course).write({
                        'scorm_entry_point': entry_point,
                    })
        return res
