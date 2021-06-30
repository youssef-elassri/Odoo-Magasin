from odoo import  fields, models

class Client(models.Model):
    _name = 'test_magasin.client'


    name = fields.Char('nom')
    prenom = fields.Char('prenom')
    date_naiss = fields.Date('Date de Naissance')
    date_rej = fields.Date('Date')
    salaire = fields.Float('salaire')
    fonc = fields.Char('fonc')

    Orders = fields.One2many(
        'test_magasin.order', 'demandeur', string='Orders ')

