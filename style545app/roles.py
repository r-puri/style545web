from rolepermissions.roles import AbstractUserRole
class Stylist(AbstractUserRole):
    available_permissions = {
        'create_style': True,
    }

class Admin(AbstractUserRole):
    available_permissions = {
        'create_style': True,
        'create_user':True,
    }
