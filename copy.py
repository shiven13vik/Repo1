# shallow copy : only one level deep, only references of nested child objects
#  deep copy : full independent copy

# shallow copy






# copying with custom object

import

class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    p1 = Person("ALex", 27)
    p2 = p1

    p2.age = 28
    print(p2.age)
    print(p2.age)









