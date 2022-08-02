from odoo import fields, models, api
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)


class session(models.Model):
    _name = 'opentutorial.session'
    _description = 'opentutorial session'

    name = fields.Char(required=True)
    description = fields.Char()
    start_date = fields.Date(default=fields.date.today())
    duration = fields.Float()
    seats = fields.Integer()
    active = fields.Boolean(default=True)

    # related fields
    instructor = fields.Many2one('res.partner', domain = ['|', ('instructor', '=', True),
                     ('teacher', 'ilike', "Teacher")])

    courses = fields.Many2one('opentutorial.course')
    # one session have many courses
    # list of course will appear on courses field in session form
    attendees = fields.Many2many('res.partner')

    # computed fields
    taken_seats = fields.Char(compute='_taken_seats')

    @api.depends('attendees', 'seats')
    def _taken_seats(self):
        _logger.info("----- %s -----", self)
        for r in self:
            _logger.info("----- seats: %s -----", r.seats)
            _logger.info("----- attendees: %s -----", r.attendees)
            if not r.seats:
                r.taken_seats = "0.0%"
            else:
                x = 100 * len(r.attendees) / r.seats
                r.taken_seats = str(x) + '%'


    @api.onchange('attendees', 'seats')
    def _check_seats(self):
            if self.seats < 0:
                return{
                    'warning': {
                        'title':'Invalid number',
                        'message':'Put correct number'
                    }
                }
            elif self.seats < len(self.attendees):
                return {
                    'warning' : {
                        'title':"too many participants",
                        'message' : "add more seats"
                    }
                }


    @api.constrains('attendees','instructor')
    def _check_instructor(self):
        for r in self:
            if r.instructor in r.attendees:
                raise ValidationError('Instructor cannot be in attendees')






