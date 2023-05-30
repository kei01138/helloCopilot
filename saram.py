# display people information
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)
people = []
people.append(Person("Hannah", 38))
people.append(Person("Sally", 23))
people.append(Person("Peter", 52))
people.append(Person("Mary", 19))
people.append(Person("John", 32))
for person in people:
    person.display()
