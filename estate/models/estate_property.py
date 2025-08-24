from odoo import fields, models

class Property(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
   

    name = fields.Char('Property Name', required=True, translate=True)
   
