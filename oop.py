# A class is a blueprint for creating objects
# objects are instances of a class

class Students:
   def __init__(self,name,gender,age):
       self.name=name
       self.gender=gender
       self.age=age
   def sayhello(self):
       print("my name is",self.name,"a",self.gender,"gender",self.age,"years")

myobje=Students("Kibet","male",22)
myobje.sayhello()


