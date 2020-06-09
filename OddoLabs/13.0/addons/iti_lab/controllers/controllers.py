# -*- coding: utf-8 -*-
# from odoo import http


# class ItiLab(http.Controller):
#     @http.route('/iti_lab/iti_lab/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iti_lab/iti_lab/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iti_lab.listing', {
#             'root': '/iti_lab/iti_lab',
#             'objects': http.request.env['iti_lab.iti_lab'].search([]),
#         })

#     @http.route('/iti_lab/iti_lab/objects/<model("iti_lab.iti_lab"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iti_lab.object', {
#             'object': obj
#         })
