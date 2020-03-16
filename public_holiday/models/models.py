# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import Warning





class PublicHoliday(models.Model):
    _name = 'public_holiday.public_holiday'
    _rec_name = 'holiday_name'


    holiday_name = fields.Char(string='Holiday Name')
    date_from = fields.Date(string='Start holiday')
    date_to = fields.Date(string='End holiday')
    total = fields.Integer(string='Number of Days')

    # employee_id = fields.Many2many('hr.employee',store=True)
    #
    #
    # @api.model
    # def create(self, vals):
    #     result=super(PublicHoliday, self).create(vals)
    #     employees=self.env['hr.employee'].search([])
    #     for employee in employees:
    #
    #         result.employee_id=[(4,employee.id)]
    #         print(result.employee_id)
    #
    #     return result



    @api.onchange('date_from','date_to')
    def calculate_date(self):
        for rec in self:
            if rec.date_from and rec.date_to:
                date_from = datetime.strptime(str(rec.date_from), '%Y-%m-%d')
                date_to = datetime.strptime(str(rec.date_to), '%Y-%m-%d')

                total = date_to - date_from
                rec.total = int(total.days+1)





