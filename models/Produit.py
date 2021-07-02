from odoo import  fields, models, api

class Produit(models.Model):

    _name='test_magasin.produit'
    img = fields.Binary('Product image')
    name = fields.Char('Product Name')
    code = fields.Char('Product Code')
    cost = fields.Float('Cost')
    prix = fields.Float('Prix de vente')

    order_lines = fields.One2many(
        'test_magasin.order_line', 'produit', string='Produit')

