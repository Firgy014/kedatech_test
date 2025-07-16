# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class registrasi_material(models.Model):
#     _name = 'registrasi_material.registrasi_material'
#     _description = 'registrasi_material.registrasi_material'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
