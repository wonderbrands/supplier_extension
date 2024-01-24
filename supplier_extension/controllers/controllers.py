# -*- coding: utf-8 -*-
# from odoo import http


# class SupplierExtension(http.Controller):
#     @http.route('/supplier_extension/supplier_extension', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/supplier_extension/supplier_extension/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('supplier_extension.listing', {
#             'root': '/supplier_extension/supplier_extension',
#             'objects': http.request.env['supplier_extension.supplier_extension'].search([]),
#         })

#     @http.route('/supplier_extension/supplier_extension/objects/<model("supplier_extension.supplier_extension"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('supplier_extension.object', {
#             'object': obj
#         })
