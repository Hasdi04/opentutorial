# -*- coding: utf-8 -*-
# from odoo import http


# class Opentutorial(http.Controller):
#     @http.route('/opentutorial/opentutorial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/opentutorial/opentutorial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('opentutorial.listing', {
#             'root': '/opentutorial/opentutorial',
#             'objects': http.request.env['opentutorial.opentutorial'].search([]),
#         })

#     @http.route('/opentutorial/opentutorial/objects/<model("opentutorial.opentutorial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('opentutorial.object', {
#             'object': obj
#         })
