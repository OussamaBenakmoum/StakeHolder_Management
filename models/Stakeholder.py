from email.policy import default
from odoo import models, fields, api
from datetime import datetime, timedelta


class Stakeholder(models.Model):
    _name = 'register.stakeholder'
    _inherit = ["mail.thread"]
    _description = 'Une partie prenante'

    name = fields.Char(string="Nom", required=True)

    user_id = fields.Many2one('res.users',
                              string='Compte associé',
                              default=lambda self: self.env.uid, help="Check that the account is already created, and that you gave it the access rights")

    project = fields.Many2one('project.project',string='Projets',default=lambda self: self.env.uid,help="select the project")
    type = fields.Selection(string='Type',
                                    selection=[('interne', 'Interne'),
                                               ('externe', 'Externe')])
    role = fields.Char(string="Role", required=True)
    interet = fields.Selection(string='Interet',
                                    selection=[('eleve', 'Elevé'),
                                               ('moyen', 'Moyen'),
                                               ('faible','Faible')])#Elevé, faible, moyen
    pouvoir = fields.Selection(string='Pouvoir',
                                    selection=[('eleve', 'Elevé'),
                                               ('moyen', 'Moyen'),
                                               ('faible','Faible')])#Elevé, faible, moyen#Elevé, faible, moyen
    strategie = fields.Selection(string='Stratégie',
                                    selection=[('acteur_cle', 'Acteur clé'),
                                               ('garder_informe', 'Garder informé'),
                                               ('effort_minimal','Effort minimal'),
                                               ('garder_satisfait','Garder satisfait')]) #Acteur clé, garder informé, effort minimal, Garder satisfait
    contribution = fields.Char(string="Contributions", required=True)
    attente = fields.Char(string="Attentes", required=True)
    actions = fields.Char(string="Actions", required=True)
    contact = fields.Char(string="Contact", required=True)



