from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class StockAPIParpameters(models.Model):
    _name = 'stock.api.parameters'

    url = fields.Char(string="Url", required=True, default='https://yfapi.net/v7/finance/options/', readonly=True)
    api_key = fields.Char(string="API Key", required=True,)
    active_rec = fields.Boolean(string="Active")

    # override create to make just on record active
    @api.model_create_multi
    def create(self, vals):
        res = super(StockAPIParpameters, self).create(vals)
        records = self.env['stock.api.parameters'].search([('id', '!=', res.id)])
        if vals[0]['active_rec'] == True:
            for rec in records:
                rec.write({'active_rec': False})
        return res

    def get_params(self):
        params = self.env['stock.api.parameters'].search([('active_rec', '=', True)], limit=1)
        if params.id != False:
            url = params.url
            api_key = params.api_key
        else:
            raise ValidationError(_('No Stock API Parameters found, you should add them From Stock System Parameters view.'))

        return {'url': url, 'api_key': api_key}






