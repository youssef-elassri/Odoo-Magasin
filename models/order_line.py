from odoo import fields, models, api

class Order_line(models.Model):
    _name = 'test_magasin.order_line'

    produit = fields.Char('Produit')
    qte = fields.Integer('qte')
    prix = fields.Float('Prix Unitaire')
    subtot = fields.Float('Sub Total', compute='_cmp_subtot')
    tva = fields.Selection([
        ('2.5', 2.5)
    ])
    tot_taxe = fields.Float('Sub Total Taxé', compute='_cmp_tax_sub')
    unite = fields.Char('unité')

    order = fields.Many2one(
        'test_magasin.order', string='Order',
        index=True, ondelete='cascade', required=True)


    @api.model
    def _cmp_subtot(record):
        for rec in record:
            if rec:
                rec.subtot = rec.prix * rec.qte

    def _cmp_tax_sub(self):
        for rec in self:
            if rec:
                 rec.tot_taxe = rec.subtot * (float(rec.tva) / 100)
