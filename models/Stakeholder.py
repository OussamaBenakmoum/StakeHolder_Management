from email.policy import default
from odoo import models, fields, api
from datetime import datetime, timedelta


class Stakeholder(models.Model):
    _name = 'register.stakeholder'
    #_inherit = ["res.partner"]
    #channel_ids = fields.Many2many('mail.channel', 'mail_channel_profile_partner', 'partner_id', 'channel_id', copy=False)
    _description = 'Une partie prenante'
    name = fields.Char(string="Nom", required=True)
    type = fields.Selection(string='Type',
                                    selection=[('interne', 'Interne'),
                                               ('externe', 'Externe')])
    role = fields.Char(string="Role", required=True)
    interet = fields.Selection(string='Interet',
                                    selection=[('eleve', 'Elevé'),
                                               ('moyen', 'Moyen'),
                                               ('faible','Faible')])#Elevé, faible, moyen
    pouvoir = fields.Selection(string='Interet',
                                    selection=[('eleve', 'Elevé'),
                                               ('moyen', 'Moyen'),
                                               ('faible','Faible')])#Elevé, faible, moyen#Elevé, faible, moyen
    strategie = fields.Selection(string='Interet',
                                    selection=[('acteur_cle', 'Acteur clé'),
                                               ('garder_informe', 'Garder informé'),
                                               ('effort_minimal','Effort minimal'),
                                               ('garder_satisfait','Garder satisfait')]) #Acteur clé, garder informé, effort minimal, Garder satisfait
    contribution = fields.Char(string="Contributions", required=True)
    attente = fields.Char(string="Attentes", required=True)
    actions = fields.Char(string="Actions", required=True)
    contact = fields.Char(string="ontact", required=True)



