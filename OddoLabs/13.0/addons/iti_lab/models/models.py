# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api
from odoo.exceptions import ValidationError



class Calls(models.Model):
    _name="iti_lab.calls"
    _description="CDR"
    # _rec_name="start_time"

    start_time=fields.Datetime()
    stop_time=fields.Datetime()
    duration=fields.Float(compute='_compute_duration',
    store=True
     )
    
    
    
    source=fields.Char()
    destination=fields.Char()
    name=fields.Char(default="New")
    station=fields.Many2one(comodel_name="iti_lab.station")
    tags=fields.Many2many(comodel_name="iti_lab.tags")
    
    state = fields.Selection(
       
        [('draft', 'Draft'), ('invoiced', 'Invoiced')],
        
        default='draft',
        string="Status"
        
    )
    
  


    @api.constrains('stop_time')
    def _check_stop_time(self):
        for record in self:
            if record.stop_time <record.start_time :
                raise ValidationError("stop time should be bigger than start time")


    
    @api.depends('start_time','stop_time')
    def _compute_duration(self):
        for record in self:
            if record.stop_time and record.start_time:
                record.duration = (record.stop_time - record.start_time).seconds / 60


class Station(models.Model):
    _name="iti_lab.station"

    name = fields.Char()
    calls=fields.One2many(comodel_name="iti_lab.calls",inverse_name="station")


class Tags(models.Model):
    _name="iti_lab.tags"


    name = fields.Char()
    
    
    
    
