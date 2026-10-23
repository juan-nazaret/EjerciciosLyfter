from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name, role):
        self._name = name
        self._role = role

    @abstractmethod
    def get_role(self):
        return self._role
    
    @abstractmethod
    def has_permission(self,permission):
        pass


class AdminUser(User):
    def __init__(self, name):
        self._role = 'Admin'
        super().__init__(name,self._role)

    def get_role(self):
        return self._role

    def has_permission(self, permission):
            if permission in ['read','write','delete']:
                return True
            else:
                return False
    
    

class RegularUser(User):
    def __init__(self, name):
        self._role = 'Regular user'
        super().__init__(name, self._role)

    def get_role(self):
            return self._role

    def has_permission(self, permission):
        if permission in ['read']:
            return True
        else: 
            return False
        
admin = AdminUser('Adrian')
print(admin.get_role())
print(admin.has_permission('write'))

user = RegularUser('Astrid')
print(user.get_role())
print(user.has_permission('delete'))