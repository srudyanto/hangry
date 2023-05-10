# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
# This addons using icecream for debugging
from icecream import ic

class StockLocation(models.Model):
    _inherit = 'stock.location'

    manager_id = fields.Many2one('res.users','Manager')


class StockPicking(models.Model):
    _inherit = 'stock.picking'


    #inherit button_validate function
    def button_validate(self):
        managers = []
        if (self.picking_type_id.code == "outgoing") or (self.picking_type_code == "internal" and self.location_dest_id.usage == "transit"):
            location = self.location_id
            parent = location.location_id
            while(parent != False):
                ic(location.name, parent.name)
                if location.manager_id:
                    managers.append(location.manager_id)
                ic(managers)
                location = parent
                parent = location.location_id
                if location.name == False:
                    break
        elif (self.picking_type_id.code == "incoming") or (self.picking_type_code == "internal" and self.location_id.usage == "transit"):
            location = self.location_dest_id
            parent = location.location_id
            while(parent != False):
                ic(location.name, parent.name)
                if location.manager_id:
                    managers.append(location.manager_id)
                ic(managers)
                location = parent
                parent = location.location_id
                if location.name == False:
                    break
        if (self.env.user in managers) : # allow when in managers list or internal transfers
            super(StockPicking, self).button_validate()
        else:
            raise ValidationError("Anda tidak berhak untuk validasi di lokasi ini")
