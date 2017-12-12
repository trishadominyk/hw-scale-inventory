# -*- coding: utf-8 -*-
from odoo import http

# class HwScaleInventory(http.Controller):
#     @http.route('/hw_scale_inventory/hw_scale_inventory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hw_scale_inventory/hw_scale_inventory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hw_scale_inventory.listing', {
#             'root': '/hw_scale_inventory/hw_scale_inventory',
#             'objects': http.request.env['hw_scale_inventory.hw_scale_inventory'].search([]),
#         })

#     @http.route('/hw_scale_inventory/hw_scale_inventory/objects/<model("hw_scale_inventory.hw_scale_inventory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hw_scale_inventory.object', {
#             'object': obj
#         })