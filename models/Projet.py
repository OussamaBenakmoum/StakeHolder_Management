from email.policy import default
from odoo import models, fields, api
from datetime import datetime, timedelta

class Projet(models.Model):
    _name = 'register.project'
    _inherit = 'project.project'
    _description = 'Une partie prenante'

    user_id = fields.Many2one('res.users',
                              string='Assigned tooooo',
                              default=lambda self: self.env.uid,
                              index=True, tracking=True)