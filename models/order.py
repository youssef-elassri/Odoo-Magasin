from odoo import fields, models, api


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
    approbateur = fields.Many2one(
        'test_magasin.employees', String='Approbateur',
        index=True, ondelete='cascade', required=True
    )

    Order_lines = fields.One2many(
        'test_magasin.order_line', 'order', string='Order Lines')


    total = fields.Float('Total', compute='_cmp_total')
    net_payer = fields.Float('Net a payer', compute='_cmp_total')
    total_taxes = fields.Float('Total Taxes', compute='_cmp_total')



    @api.model
    def _cmp_total(self):
        for rec in self.Order_lines:
            if rec:
                self.total += rec.subtot
                self.total_taxes += rec.tot_taxe

        self.net_payer = self.total + self.total_taxes

