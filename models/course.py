from odoo import models, fields

class Course(models.Model):
    _name = 'opentutorial.course'
    _description = 'opentutorial course'

    title = fields.Char(required=True)
    description = fields.Char()

    responsible = fields.Many2one('res.users')
    session = fields.One2many('opentutorial.session', 'courses')


