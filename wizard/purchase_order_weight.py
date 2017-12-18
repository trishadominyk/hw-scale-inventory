# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError
import math

class ChangePurchaseOrderWeight(models.TransientModel):
	_name = 'purchase.order.weight'
	_description = 'Purchase order set product_qty with weighing scale'

	purchase_id = fields.Many2one('purchase.order.line', string='Description', required=True, readonly=True)
	product_qty = fields.Float(digits=(5, 2), string='Quantity', required=True)

	@api.model
	def default_get(self,fields):
		res = super(ChangePurchaseOrderWeight, self).default_get(fields)
		if 'purchase_id' in fields and not res.get('purchase_id') and self._context.get('active_model') == 'purchase.order.line' and self._context.get('active_id'):
			res['purchase_id'] = self._context['active_id']
		if 'product_qty' in fields and not res.get('product_qty') and res.get('purchase_id'):
			res['product_qty'] = self.env['purchase.order.line'].browse(res.get('purchase_id')).product_qty

		return res

	@api.multi
	def set_weight(self):
		for wizard in self:
			order = wizard.purchase_id
			order.write({'product_qty': wizard.product_qty})
		return {}

