# -*- coding: utf-8 -*-

{
    'name': 'Alipay Payment Acquirer',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: Alipay Implementation',
    'version': '1.0',
    'description': """Alipay Payment Acquirer""",
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_alipay_templates.xml',
        'views/account_config_settings_views.xml',
        'data/payment_acquirer_data.xml',
    ],
    'installable': True,
}
