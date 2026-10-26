from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name):
        self._name = name

    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def has_permission(self,action):
        pass


class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return 'Admin'

    def has_permission(self,action):
        return action != ""
            
    
    

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
            return 'Regular User'

    def has_permission(self, action):
        return action in ['read']
        
        
admin = AdminUser('Adrian')
print(admin.get_role())
print(admin.has_permission('write'))

user = RegularUser('Astrid')
print(user.get_role())
print(user.has_permission('delete'))