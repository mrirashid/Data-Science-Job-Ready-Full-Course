## checking the equality of two objects
class User:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.id == other.id

u1 = User(1)
u2 = User(2)
u3 = User(1)
print(u1 == u2)
print(u1 == u3)


