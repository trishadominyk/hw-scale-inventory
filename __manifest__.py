# -*- coding: utf-8 -*-
{
    'name': "Weighing Scale with Inventory",

    'summary': """
        Hardware Driver for Weighing Scales implementation in Inventory""",

    'description': """
        This allows the Weighing Scale Driver to be recognized in the Inventory module for inventory adjustments
        and inputting weight data.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock','hw_scale','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'wizard/product_stock_weight.xml',
        'wizard/purchase_order_weight.xml',
        'views/product_template_stock_inherit.xml',
        'views/purchase_order_form_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}