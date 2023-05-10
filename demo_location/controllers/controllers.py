# -*- coding: utf-8 -*-
# from odoo import http


# class DemoLocation(http.Controller):
#     @http.route('/demo_location/demo_location', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_location/demo_location/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_location.listing', {
#             'root': '/demo_location/demo_location',
#             'objects': http.request.env['demo_location.demo_location'].search([]),
#         })

#     @http.route('/demo_location/demo_location/objects/<model("demo_location.demo_location"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_location.object', {
#             'object': obj
#         })
