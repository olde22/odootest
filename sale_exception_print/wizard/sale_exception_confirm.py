##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, api


class SaleExceptionConfirm(models.TransientModel):

    _inherit = 'sale.exception.confirm'

    @api.multi
    def action_confirm(self):
        if self.ignore and self._context.get('print_exceptions', False):
            self.related_model_id.ignore_exception_print = True
            # con esto limpiamos el ignore para que no super no ignore todo
            self.ignore = False
        return super(SaleExceptionConfirm, self).action_confirm()
