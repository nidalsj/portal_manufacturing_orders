{
    'name': 'Portal Manufacturing Orders',
    'summary': 'Adds Manufacturing Orders to the customer portal',
    'version': '17.0.1.0.0',
    'category': 'Website',
    'license': 'LGPL-3',
    'depends': ['portal', 'mrp', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/mo_portal_template.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}