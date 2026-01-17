## obj1+ obj2
class Vector:
    def __init__(self,w1,w2):
        self.w1 = w1
        self.w2 = w2
    def __str__(self):
        return f"{self.w1}i + {self.w2}j"
    def __add__(self,other):
        return Vector(self.w1 + other.w1, self.w2 + other.w2)

v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = v1 + v2
print(v3)






