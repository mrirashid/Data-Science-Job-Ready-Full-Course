## Super and Proxy 
class User:
    def __init__(self, name):
        self.name = name
        self.role = "User"
class Admin(User):
    def __init__(self, name, level):
        super().__init__(name) 
        self.level = level
        self.role = "Admin"
admin = Admin("Rashid", "Super")

print(admin.name)
print(admin.role)
print(admin.level)
