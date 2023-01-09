class Animal:
    def __init__(self):
        self.age=1

    def eat(self):
        print("eat")


class Mammal(Animal):

   def walk(self):
        print("walk")

m= Mammal()
print(m.eat())

#isinstance()-built in function it tells us if an object is a instance of given class 
# so here if we check below both will true as mammal derived from animal
print(isinstance(m,Mammal))
print(isinstance(m,Animal))
print(isinstance(m,object))
o=object()

#object class - is a base class for all classes of python it directly or indirectly derived from object class
#issubclass it will be true
print(issubclass(Mammal,object))
#method overriding - same method in both the class so method overriding 
#means replacing or extending the method defined in base class.
class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age=1

    def eat(self):
        print("eat")


class Mammal(Animal):

    def walk(self):
        print("walk")

    def __init__(self):
        super().__init__()
        print("Mammal constructor")
        self.weight= 2

m=Mammal()
print(m.age)
print(m.weight)

#Multilevel inheritance 1 2 3 4 5... level its not good increase complexity
#Multiple inheritance
class employee:
    def Greet(self):
        print("Employee Greet")
 
class person:
    def Greet(self):
        print("Person Greet")

class Manager(person,employee):
    pass

manager=Manager()
manager.Greet()

#good example of python Inheritance- that have less multilevel inheritance
#lets take an example want to model the concept of a stream of data.read the stream of data from a file,from network
#from the memory All these streams have a few things in common, we can open them,we can open them we can close them
#we can close data from them how we read data from a stream. but how we read data from stream is dependant upon the 
#type of the stream, because reading data from a file is different then reading it from a network.
#supo
class InvalidOperationError(Exception):
    pass

class stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            #below is the custom exception because python don't have built in 
            raise InvalidOperationError("Stream is already opened")

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened= False

class Filestream(stream):
      def read(self):
        print("Reading data from a file")
   
class NetworkStream(stream):
      def read(self):
        print("Reading data from a Network")



#Abstract Base Class- its purpose to provide some common code 
# error we got TypeError: Can't instantiate abstract class stream with abstract method read
#
from abc import ABC,abstractmethod

class InvalidOperationError(Exception):
    pass

class stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            #below is the custom exception because python don't have built in 
            raise InvalidOperationError("Stream is already opened")

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened= False
    
    @abstractmethod
    def read(self):
        pass

class Filestream(stream):
      def read(self):
        print("Reading data from a file")
   
class NetworkStream(stream):
      def read(self):
          print("Reading data from a Network")

class MemoryStream(stream):
    pass
#NameError: name 'Memorystream' is not defined. Did you mean: 'MemoryStream'? in below code
# stream = MemoryStream()
#stream.open()

#Polymorphism
from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw (self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

#Duck Typing
#python will check that we have the for loop so controls should be iterable like dictionary,list,tuple. 
#and it should have draw method so it how python work if it wlak like duck talk like duck python will be happy
#and it doesn't check for type of object check existance of certain methods in our object.
#
def draw(controls):
   for control in controls:
    control.draw()

ddl=DropDownList()
TextBox = TextBox()
draw([ddl,TextBox])

#Extending Built - in Types.
class Text(str):
    def duplicate(self):
        return self +self

#extending append method of list class
class TrackableList(list):
    def append(self,object):
        print("Append Called")
        super().append(object)

text = Text("Python")
print(text.lower())
print(text.duplicate())

#Data classes - we use classes to bundle data and functionality in one unit Now as you work on larger programme
#you may have classes that only have data not behaviour
# wrriting init and __eq__ method for data classes is little bit tidious
class Point:
    def __init__(self,x,y):
        self.x=x 
        self.y=y 
      #magic method
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y 

p1=Point(1,2)
p2=Point(1,2)
print(id(p1))
print(id(p2))
print(p1==p2)
#If you are dealing with classes that no method no behaviour and have data ,you can use a main couple instance, let me
#lets see how we can do that
from collections import namedtuple

Point= namedtuple("Point", ["X", "Y"])
#first thing here our code is more clear and more ambigeous so this keyword object make our code more redable argument 
#made our code more clear second benefit is that we dont have to explicitly implement a magic method to compare 2 objects 
#so if we have 2 point object with exact same attribute 
p1= Point(X=1,Y=2)
p2= Point(1,2)
print(p1==p2)
#if u are working with classes that only have data and no methods, you might want to use nametuple instead
#you will write less code and this name tuple and this name tuples are better then regular tuples, because here 
#we will have attributes in point object just like the attribute we have in our classes if we print p1.x we see 1 
#this values are immutable we get the attribute error.






