## __variable __
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password   

# Create object
user = User("Rashid", "12345")
print(user.username)
print(user._User__password)

    