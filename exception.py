try:
    file=open("Exception.py")
    age = int(input("Age:"))
    Xfactor = 10/age
except ValueError as ex:
    print("you didn't enter a valid age.")
    print(ex)
    print(type(ex))
except (ZeroDivisionError,ValueError):
    print("you didn't enter a valid age.")
else:
    print("No exceptions were throw.")
    print("Execution of programme continue")
finally:
 file.close()

 #with statement- we can avoid using finally statement
 #with statement automatically release external resources so need for finnaly clause.
 #if we want to open another file with open("Exception.py") as file: ,open("another.txt") as target:
try:
    with open("Exception.py") as file:       
     #context management protocol or ifan object have this two methods like file.__exit and file.__enter
      age = int(input("Age:"))
      Xfactor = 10/age
except ValueError as ex:
    print("you didn't enter a valid age.")
    print(ex)
    print(type(ex))
except (ZeroDivisionError,ValueError):
    print("you didn't enter a valid age.")
else:
    print("No exceptions were throw.")
    print("Execution of programme continue")

#Raising Exception you can raise and throw exception in your own function
#google python 3 built in exception search from googke u will find complete list of exception
code1= """
def calculate_Xfactor(age):
    if age<=0:
        raise ValueError
    return 10/age

try:
    calculate_Xfactor(-1)
except ValueError as error:
    print(error)
"""
#Cost of raising exception- prefer not raise exception because this exceptions come with a cost
#if we dont raise exception code will be almost 4 times faster so
from timeit import timeit
print("First code", timeit(code1,number=10000))






