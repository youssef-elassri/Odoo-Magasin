from odoo import  fields, models

class Client(models.Model):
    _name = 'test_magasin.employees'


    name = fields.Char('nom')
    prenom = fields.Char('prenom')
    dateNaiss = fields.Date('Date de naissance')
    dateJoin = fields.Date('joinning date')
    post = fields.Char('post')
    salaire = fields.Float('salaire')

    Orders = fields.One2many(
        'test_magasin.order', 'approbateur', string='Orders')