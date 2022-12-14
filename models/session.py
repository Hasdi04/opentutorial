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
    instructor = fields.Many2one('res.partner')
    courses = fields.Many2one('opentutorial.course')
    # one session have many courses
    # list of course will appear on courses field in session form
    attendees = fields.Many2many('res.partner')

    # DO NOT DELETE
    def test(self):
        pass

    # TO DELETE
    def test2(self):
        pass