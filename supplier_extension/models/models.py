# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class supplier_extension(models.Model):
    _inherit = 'account.move'

    l10n_mx_edi_supplier_cfdi_uuid = fields.Char(string="Folio fiscal proveedor",help="En este campo se agregara el folio fiscal de la factura proveedor")

    _sql_constraints = [
        ('unique_l10n_mx_edi_supplier_cfdi_uuid', 'unique(l10n_mx_edi_supplier_cfdi_uuid)', 'Ya existe una factura proveedor con este folio.'),
    ]