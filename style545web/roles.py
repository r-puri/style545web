from rolepermissions.roles import AbstractUserRole
class Stylist(AbstractUserRole):
    available_permissions = {
        'create_style': True,
        'create_user':False,
        'create_item': False
    }

class Admin(AbstractUserRole):
    available_permissions = {
        'create_style': True,
        'create_user':True,
        'create_item': True
    }
class Vendor(AbstractUserRole):
    available_permissions = {
        'create_style': False,
        'create_user':False,
        'create_item': True
    }
