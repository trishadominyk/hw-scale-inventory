# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError
import math

class ChangeProductTemplateWeight(models.TransientModel):
	_name = 'product.template.weight'
	_description = 'Inventory set weight with weighing scale'

	product_id = fields.Many2one('product.template', string='Description', required=True, readonly=True)
	weight = fields.Float(digits=(5, 2), string='Quantity', required=True)

	@api.model
	def default_get(self,fields):
		res = super(ChangeProductTemplateWeight, self).default_get(fields)
		if 'product_id' in fields and not res.get('product_id') and self._context.get('active_model') == 'product.template' and self._context.get('active_id'):
			res['product_id'] = self._context['active_id']
		if 'weight' in fields and not res.get('weight') and res.get('product_id'):
			res['weight'] = self.env['product.template'].browse(res.get('product_id')).weight

		return res

	@api.multi
	def set_weight(self):
		print 'set weight function!'
		for wizard in self:
			order = wizard.product_id
			order.write({'weight': wizard.weight})
		return {}

