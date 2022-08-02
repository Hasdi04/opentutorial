from odoo import fields, models

class session(models.Model):
    _name = 'opentutorial.session'
    _description = 'opentutorial session'

    name = fields.Char(required=True)
    description = fields.Char()
    start_date = fields.Date()
    duration = fields.Float()
    seats = fields.Integer()

    # related fields
    instructor = fields.Many2one('res.partner', domain = ['|', ('instructor', '=', True),
                     ('teacher', 'ilike', "Teacher")])

    courses = fields.Many2one('opentutorial.course')
    # one session have many courses
    # list of course will appear on courses field in session form
    attendees = fields.Many2many('res.partner')
