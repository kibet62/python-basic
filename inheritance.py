# inheritance allows one class to inherit attribute
# and methods from another class
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "woof"
class Cat(Animal):
    def speak(self):
        return "meow"
# this are objects
Doggy=Dog("shakes")
Cat=Cat("whiskers")
print("the Dog bearks:",Doggy.speak())
print("the cat whises:",Cat.speak())