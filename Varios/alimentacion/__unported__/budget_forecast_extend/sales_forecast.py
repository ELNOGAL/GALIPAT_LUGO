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
from openerp.osv import osv
from openerp.tools.translate import _
class sales_forecast(osv.osv):
    _inherit = 'sales.forecast'

    def create_budget_lines2(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        budget_line = self.pool.get('budget.line')
        print "holaaaaaaaaa"
        for cur in self.browse(cr, uid, ids):
            if cur.sales_forecast_lines:
                if not cur.budget_version_id and not cur.budget_item_id:
                    raise osv.except_osv(_('Error !'), _('For create a budget line is neccessary to have a budget version and budget item at sales forecast.'))
                for line in cur.sales_forecast_lines:
                    vals = {
                        'budget_version_id': cur.budget_version_id.id,
                        'budget_item_id': cur.budget_item_id.id,
                        'name': _('Sales forecast line of ') + cur.name,
                        'product_id': line.product_id.id,
                        'amount': line.total_amount,
                        'currency_id': cur.budget_version_id.currency_id.id,
                        'jan_amount': float(round(line.jan_amount,2)),
                        'feb_amount': float(round(line.feb_amount,2)),
                        'mar_amount': float(round(line.mar_amount,2)),
                        'apr_amount': float(round(line.apr_amount,2)),
                        'may_amount': float(round(line.may_amount,2)),
                        'jun_amount': float(round(line.jun_amount,2)),
                        'jul_amount': float(round(line.jul_amount,2)),
                        'aug_amount': float(round(line.aug_amount,2)),
                        'sep_amount': float(round(line.sep_amount,2)),
                        'oct_amount': float(round(line.oct_amount,2)),
                        'nov_amount': float(round(line.nov_amount,2)),
                        'dec_amount': float(round(line.dec_amount,2)),
                        'analytic_account_id': cur.analytic_id and cur.analytic_id.id or False
                    }
                    budget_line.create(cr, uid, vals)

        return True

    def action_validate(self, cr, uid, ids, context=None):

        self.create_budget_lines2(cr, uid, ids, context)

        return super(sales_forecast, self).action_validate(cr, uid, ids, context=context)
sales_forecast()