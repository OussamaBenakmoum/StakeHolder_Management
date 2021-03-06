# -*- coding: utf-8 -*-
# //////////////////////////////////////////////////////////////////////////////
#
#    ESI ALger.
#
#    Copyright (C) 2022-TODAY.
#    Author: Oussama BENAKMOUME && TAHAR Noureddine,
#
# //////////////////////////////////////////////////////////////////////////////

{
    'name': "Stakeholder Management",
    'version': '1.0.0',
    'summary': """Gestion des parties prenantes""",
    'description': """
       Module de gestion du registre des parties prenantes, TP pour un module de gestion de changement dans un projet.
    """,
    'author': 'BENAKMOUME Oussama AND TAHAR Noureddine',
    'company': 'ESI Alger groupe = SIT4',
    'depends': ['mail','project','calendar'],
    'data': [
        'views/registres.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
    ],
    'demo': [],
    'images': [],
    'installable': True,
    'application': True
}
