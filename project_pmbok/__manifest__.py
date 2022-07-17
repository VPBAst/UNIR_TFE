# -*- coding: utf-8 -*-
{
    'name': "project_pmbok",

    'summary': """
        Modulo para la gestion de proyectos basada en la guía PMBOK""",

    'description': """
        Modulo para la gestion de proyectos basada en la guía PMBOK
    """,

    'author': "Victor Patallo",
    'website': "http://www.unir.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # aplicacion:  conjunto de modulos, con una funcionalidad mayor
    #'application': True,
}

