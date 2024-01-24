# -*- coding: utf-8 -*-
{
    'name': "Automatic Checkout Attendance",

    'summary': """
        This model is for Attendance module customization""",

    'description': """
        -Customize as per BCN requirements.
        -Update automatic checkout.
    """,

    'author': "Kamrul Islam Shahin",
    'website': "https://bcnvisuals.com/",
    'license': 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Human Resources',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr', 'hr_attendance'],

    # always loaded
    'data': [
        'data/automatic_checkout_attendance_scheduler.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'qweb': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}