## Class variables vs instance variables

class Person:
    species = "Human"
p1 = Person()
p2 = Person()

p1.name = "A"
p2.name = "B"

Person.species = "Rashidul"
print(p1.species)
print(p2.species)
print(Person.species)




