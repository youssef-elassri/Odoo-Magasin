from odoo import  fields, models

class Order(models.Model):
    _name = 'test_magasin.order'


    name = fields.Char('Ref')
    demandeur = fields.Many2one(
        'test_magasin.client', String='Demandeur',
        index=True, ondelete='cascade', required=True
    )
    date = fields.Date('Date')
    etat = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('confirmed', 'confirmed'),
        ('done', 'done'),
    ], default='draft', index=True)
    approbateur = fields.Char('Approbateur')

    Order_lines = fields.One2many(
        'test_magasin.order_line', 'order', string='Order Lines')




class Oreder_line(models.Model):
    _name = 'test_magasin.order_line'

    produit = fields.Char('Produit')
    qte = fields.Integer('qte')
    unite = fields.Char('unité')

    order = fields.Many2one(
        'test_magasin.order', string='Order',
        index=True, ondelete='cascade', required=True)
