# -*- coding: utf-8 -*-
{
    'name': "Supplier Extension",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Wonderbrands",
    'website': "http://www.wonderbrands.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'account_accountant'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
