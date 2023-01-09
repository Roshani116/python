#class: Blueprint for creating a new object.
#object:instance of a class
class point:
    default_colour="red"
    #self is a reference to the current point object. using self we can read
    #x and y are attribute class level attribute is default colour class attribute shared across all the instances of class.
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #how we can define method at the class level
    #cls is the refrence to class itself @classmethod is called the decorator 
    #is the way to extend behaviuor of decorator or function.
    def __str__(self):
        return f"({self.x},{self.y})"
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __gt__(self,other):
        return self.x > other.x and self.y > other.y
    def __add__(self,other):
        return point(self.x + other.x,self.y + other.y)
    @classmethod
    def Zero(cls):
        #cls(0,0) is exactly same as calling point(0,0) the diffrence is that
        #at run time when we called the zero method pointer inturpreter will automatically pass 
        #the reference to the point class to the zero method
        #instance methods and class methods whne we run thos classmethod will get point with its initial values.
        return cls(0,0)

    def draw(self):
        print(f"Point ({self.x},{self.y})")

#some times we have an object and if we want to know if this object is of given class isinstance
#to check if point object is instance of point class in this way create point custom classes
#instance attributes 
Point = point(1,2)
print(isinstance(point,type(point)))
Point.draw()
another=point(1,2)
another.draw()
print(another.default_colour)
another.default_colour="Yellow"
print(another.default_colour)
#factory method
print(Point.Zero())
#magic methods search python3 magic methods in google__str__ object into string it convert. 
#tehy called automatically by python interpreter
#if there is no magic method defined then out would be <__main__.point object at 0x00000141B320B970>
#__init__,__str__,__repr__,
print(Point)
print(f'Normal point{Point}')
print(f'with str function point{str(Point)}')
# comparing object
#for below code will get false beacause it compare to refrences or address of this 2 objects in a memory
#so 2 diffrent references hence return false
Point1=point(1,2)
Point2=point(1,2)
print(Point1==Point2)
#so in this case we will use magic methods __eq__, more methods for diff use __ne__,__lt__,__qt__
Point1=point(10,20)
Point2=point(1,2)
print(Point1>Point2)
#performing Arithmatic operators- magic method __add__
print(Point1+Point2)
#Making custom containers
#why we created the custom class instead of using typical dictionary
#dictionary will show diffrent count if the same words are case sensitive.
#to handle this we created customer class where we can covert value to lower case  while reading and getting input
class __tagCloud:
    def __init__(self):
        self.__tags={}

    def add(self,__tag):
      self.__tags[__tag.lower()]= self.__tags.get(__tag.lower(),0)+1
#if you want to implement count of __tag like this cloud["python"] for this define _getitem
    def __getitem__(self,____tag):
        return self.__tags.get(__tag.lower(),0)
    
    def __setitem__(self,__tag,count):
        self.__tags[__tag.lower()] = count
    
    def __len__(self):
        return len(self.__tags)
    #what iter function will do it walks you to through container
    #if we prefix __before metghods we make them private
    def __iter__(self):
        return iter(self.____tags)


    
     

cloud=__tagCloud()
# to get this we have defined the above all methods
cloud["Python"]=10
cloud.add("Python")
cloud.add("python")
cloud.add("Python")
cloud.add("Python")
cloud.add("python")
# print(cloud.__tags) as it is private will get an error
#we can make private member of class
#properties-> you have to control over atribute of class
#for example if you are giving negative value of price -50 and python interpreter will execute that it will not have 
#any problem.
#one way to do this
class product:
    def __init__(self,price):
       self.set_price(price)
    
    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative.")
        self.__price=value

product=product(50)
product.price=1
print(product.price)
#another way to avoid negative value of price property

class Product1:
    def __init__(self,price):
        self.price=price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price=value
     
Product1 = Product1(-50)
print(Product1.price)




