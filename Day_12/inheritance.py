## Inheritance
class User:
    def role(self):
        return "User"
class Admin(User):
    def role(self):
        return "Admin"
user = User()
admin = Admin()
print(user.role())
print(admin.role())

 