from email.policy import default
from odoo import models, fields, api
from datetime import datetime, timedelta

class Projet(models.Model):
    _name = 'register.project'

    _description = 'Une partie prenante'