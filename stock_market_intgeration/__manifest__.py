# -*- coding: utf-8 -*-
{
    'name': "Damhogy Stock Integration",

    'summary': """ Integration with Saudi Stock """,

    'description': """
        Enter the stock market share as product and update its price
         automatically with the last price of the daily market share
          using Yahoo finance API """,

    'author': "Ahmed Elsayed Aldamhogy",
    'category': 'Inventory',
    'version': '14.0.1',

    'depends': ['base', 'stock'],

    'data': [
        'security/ir.model.access.csv',
        'data/update_stock_share_data.xml',
        'views/stock_api_parameters.xml',
        'views/inherit_product_template.xml',
        'views/share_price_history.xml',

    ],
}
