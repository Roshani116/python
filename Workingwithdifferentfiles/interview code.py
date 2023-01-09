def mean(a,b):
    try:

        @cl
        print((a+b)/2)
    except TypeError:
        function_Error()
 
 
def square(sq):
    try:
        print(sq*sq)
    except TypeError:
       function_Error()


def function_Error():
    print("wrong data types. enter numeric")

