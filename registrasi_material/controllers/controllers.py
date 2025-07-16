# -*- coding: utf-8 -*-
# from odoo import http


# class RegistrasiMaterial(http.Controller):
#     @http.route('/registrasi_material/registrasi_material/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/registrasi_material/registrasi_material/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('registrasi_material.listing', {
#             'root': '/registrasi_material/registrasi_material',
#             'objects': http.request.env['registrasi_material.registrasi_material'].search([]),
#         })

#     @http.route('/registrasi_material/registrasi_material/objects/<model("registrasi_material.registrasi_material"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('registrasi_material.object', {
#             'object': obj
#         })
