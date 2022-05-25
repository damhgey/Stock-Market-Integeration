from odoo import api, fields, models


class SharesPricesHistory(models.Model):
    _name = 'shares.prices.history'
    _order = 'date desc'


    date = fields.Date(string='Date', required=True, index=True, default=lambda self: fields.Date.today())
    share_id = fields.Many2one('product.template', string='Share', readonly=True, required=True, ondelete="cascade")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    day_price = fields.Float(digits=0, default=1.0, string="Day Price")
    day_highest_price = fields.Float(digits=0, default=1.0, string="Highest Price")
    day_lowest_price = fields.Float(digits=0, default=1.0, string="Lowest Price")
    day_open_price = fields.Float(digits=0, default=1.0, string="Open Price")
    day_previous_close_price = fields.Float(digits=0, default=1.0, string="Previous Close Price")

