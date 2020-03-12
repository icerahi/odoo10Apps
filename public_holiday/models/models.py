# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import Warning

class PublicHoliday(models.Model):
    _name = 'public_holiday.public_holiday'

    name = fields.Char(string='Name')
    start = fields.Date(string='Start holiday')
    end = fields.Date(string='End holiday')
    total = fields.Integer(string='Number of Days')


    @api.onchange('start','end')
    def calculate_date(self):
        for rec in self:
            if rec.start and rec.end:
                start = datetime.strptime(str(rec.start), '%Y-%m-%d')
                end = datetime.strptime(str(rec.end), '%Y-%m-%d')

                total = end - start
                rec.total = int(total.days+1)





