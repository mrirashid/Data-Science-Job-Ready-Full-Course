import pickle
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Rashidul", 23)

with open("user.pkl", "wb") as f:
    pickle.dump(user, f)
