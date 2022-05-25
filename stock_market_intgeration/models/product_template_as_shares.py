import requests
from odoo import fields,models,api,_
from .stock_api_parameters import StockAPIParpameters as params



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_share = fields.Boolean(string="Can be Share", default=True)
    share_prices_ids = fields.One2many('shares.prices.history', 'share_id', string='Share_prices')

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Choose another name - Product name must be unique!')
    ]

    @api.model
    def update_shares_price(self):
        # Get Shares names
        shares_ids = self.env['product.template'].sudo().search([('is_share', '=', True)])

        # Initialize Params
        url = params.get_params(self).get('url')
        api_key = params.get_params(self).get('api_key')

        headers = {'x-api-key': api_key,
                  'Content-type': 'application/json'}

        # Get stock share data by product name
        for share in shares_ids:
            share_name = share.mapped('name')[0]
            try:
                request = requests.get(url=url + share_name, headers=headers, )
                result = request.json()['optionChain']['result']
                if request.status_code == 200 and len(result) != 0:
                    data = result[0]['quote']

                    vals = {
                        'share_id': share.id,
                        'day_price': data['regularMarketPrice'],
                        'day_highest_price': data['regularMarketDayHigh'],
                        'day_lowest_price': data['regularMarketDayLow'],
                        'day_open_price': data['regularMarketOpen'],
                        'day_previous_close_price': data['regularMarketPreviousClose'],
                    }
                    self.env['shares.prices.history'].sudo().create(vals)
                    share.write({'list_price': vals['day_price']})
            except:
                pass



    def open_share_price_history(self):
        return {
            'name': _('Price History'),
            'domain': [('share_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'shares.prices.history',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
