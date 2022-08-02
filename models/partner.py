from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'



    instructor = fields.Boolean(default=False)
    sessions = fields.Many2many('opentutorial.session')

    teacher = fields.Selection([('Teacher1', 'Level 1'), ('Teacher2', 'Level 2')])

