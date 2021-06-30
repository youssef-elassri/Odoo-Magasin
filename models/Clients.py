from odoo import  fields, models

class Client(models.Model):
    _name = 'test_magasin.client'


    name = fields.Char('nom')
    prenom = fields.Char('prenom')

    Orders = fields.One2many(
        'test_magasin.order', 'demandeur', string='Orders ')

