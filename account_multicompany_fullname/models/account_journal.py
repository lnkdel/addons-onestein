# -*- coding: utf-8 -*-
# Copyright 2016 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    @api.model
    def _fullname_get(self, item):
        name = item[1] or ''
        company = self.browse(item[0]).company_id
        company_name = company and company.name or ''
        return name + ' - ' + company_name

    @api.multi
    def name_get(self):
        res = super(AccountJournal, self).name_get()
        journals = []
        for item in res:
            fullname = self._fullname_get(item)
            journals.append((item[0], fullname))
        return journals
