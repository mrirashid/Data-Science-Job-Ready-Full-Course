class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        return 2026 - self.birth_year   
user = User("Rashid", 2002)
print(user.age)  
