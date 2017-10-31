
from openerp import models, api, fields, _




class TenantTenant(models.Model):
    _name = 'tenant.tenant'
    _description = 'Room Number'

    tenant_name =  fields.Char(string="Full Name")
    room_id = fields.Many2one("room.room",string="Room Number")
    contact_number = fields.Integer(string="Contact Number")
    date_started = fields.Datetime(string='Date')
    payment_history = fields.One2many('payment.payment','tenant_name',string='Payment History')




class RoomRoom(models.Model):
    _name ='room.room'



    name = fields.Char(string="Room Number")
    amount_rental = fields.Float(string="Rental Price")
    capacity = fields.Integer(string="Capacity")



class PaymentPayment(models.Model):
    _name = 'payment.payment'


    tenant_name = fields.Many2one('tenant.tenant', string='Tenant Name')
    room = fields.Many2one('room.room', string='Room Number')
    payment = fields.Many2one('room.room', string='Payment')
    payment_sched = fields.Datetime(string='Payment Date')
    paid = fields.Boolean(string='Paid')
