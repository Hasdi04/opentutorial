from odoo import fields, models

class session(models.Model):
    _name = 'opentutorial.session'
    _description = 'opentutorial session'

    name = fields.Char(required=True)
    description = fields.Char()
    start_date = fields.Date()
    duration = fields.Float()
    seats = fields.Integer()
