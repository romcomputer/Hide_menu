
# -*- coding: utf-8 -*-
{
    'name': u'Hide Menu',
    'version': '13.0.1.0.0',
    'category': 'Hide Menu',
    'summary': '',
    'website': 'https://silentinfotech.com',
    'description': u"""

In this module hide menu and template

""",
    'author': u'Silent Infotech Pvt. Ltd.',
    'depends': [
        'base','web'
    ],

    'data': [
        'security/ir.model.access.csv',


        

    ],
    'qweb': [

        'static/src/xml/base.xml',
        'static/src/xml/gift_card.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
    'license': u'OPL-1',
}
