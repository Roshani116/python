def greet(first_name, last_name):
    print("Hi There")
    print("Welcome abroad")


greet("Mosh", "Hamedani")
greet("John", "Smith")
print("Roshani")


def greet1(First_name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"


Message = get_greeting("Mosh")
print(Message)

# Keyword arguments


def increament(number, by):
    return number + by


print(increament(2, by=1))

# By default argument- if we dont pass argument for second it will take second argument as input

# Xargs


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# XXargs
#here you can pass multiple keyword and arguments.

def save_user(**user):
    print(user)


save_user(id=1, name="John", age=22)

# Scope
# global and local variable.


def send_email(name):
    message = "b"


message = "a"

X = input("X: ")
Y = int(X) + 1
print(f"X: {X}, Y: {Y}")
# type conversion
# int(X)
# float(X)
# bool(X)
# str(X)
