# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2004-2012 Pexego Sistemas Informáticos All Rights Reserved
#    $Marta Vázquez Rodríguez$ <marta@pexego.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Stock location templates",
    "description": """
        Module that adds templates logistics flows to simplify the configuration process these into products.
        """,
    "version" : "1.0",
    "author" : "Pexego",
    "depends" : ["base", "product","stock", "stock_location"],
    "category" : "Manufacturing",
    "init_xml" : [],
    "update_xml" : ["stock_location_templates_view.xml",
                    "wizard/templates_product_view.xml",
                    "product_view.xml",
                    "security/ir.model.access.csv",
                    "security/stock_location_templates_security.xml"
                    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}