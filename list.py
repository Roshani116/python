from sys import getsizeof
from array import array
from collections import deque
from tomlkit import key


letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined1 = zeros + letters
numbers = list(range(20))
print(combined1)
print(numbers)
# list unpacking
numbers = [1, 2, 3, 8, 2, 4, 9, 7, 8, 5, 2, 3, 4, 5]
first, second, *other = numbers
print(f"List1 {first} \nSecond list {second} \n third list{other}")
# Looping over list
letters = ["a", "b", "C"]
#Often, when dealing with iterators, we also get need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task. 
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. 
#Python’s enumerate() lets you write Pythonic for loops when you need a count and the value from an iterable. 
#The big advantage of enumerate() is that it returns a tuple with the 
#counter and value, so you don’t have to increment the counter yourself. It also gives you the option to change the starting value for the counter.
#keep count of iteration also can change starting of loop.
for letter in enumerate(letters):
    print(letter)
# Add
# letter.append("D")
# letter.insert(0, "-")

# Remove
# letter.pop(0)
# letter.remove("b")
del letters[0:3]

# finding element in index
letter.count
# print(letters.index("d"))

# sorting list
numbers = [3, 4, 12, 67, 23, 45]
numbers.sort(reverse=True)

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]


def sort_item(items):
    return items[1]


items.sort(key=sort_item)
print(items)

# lambda cleaner way to define function which we are going to use only once
items.sort(key=lambda items: items[1])
print(items)


# map function
#map() function returns a map object(which is an iterator) 
#of the results after applying the given function to each item of a given iterable (list, tuple etc.)
#map(fun, iter)
#fun : It is a function to which map passes each element of given iterable.
#iter : It is a iterable which is to be mapped.
*/
# Python program to demonstrate working
# of map.
  
# Return double of n
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
*/

prices = []
for item in items:
    prices.append(item[1])
print(prices)

# how we can implement using lambda above map function
prices = list(map(lambda item: item[1], items))
# List comprehensions same result as above map statement and cleaner way
#newList = [ expression(element) for element in oldList if condition ] 
#List = [character for character in [1, 2, 3]]
# Displaying list
#print(List)
#More time-efficient and space-efficient than loops.
#Require fewer lines of code.
#Transforms iterative statement into a formula.

prices = [item[1] for item in items]
print(f" map function list{prices}")

# filter function
#filter(function, sequence)
#Parameters:
#function: function that tests if each element of a 
#sequence true or not.
#sequence: sequence which needs to be filtered, it can 
#be sets, lists, tuples, or containers of any iterators.
#Returns:
#returns an iterator that is already filtered.

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# zip function if we have 2 list we want to combine this 2 list
List1 = [1, 2, 3]
List2 = [4, 5, 6, 7]
print("Output of Zip function below:")
print(list(zip(List1, List2)))
# we can pass string as well
print(list(zip("abc", List1, List2)))
# Stack very useful in real world best example is your browser when we navigate to couple of website ad go back remove from the stack
# back butto this will remove last item from stack and return it LIFO
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.pop(1)
if not browsing_session:
    browsing_session[-1]
# Queues FIFO
# if we are dealing with large list it will have adverse effect on speed
# module is the bucket with bunch of reusable code we can say deque is a class here
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
# tuples when we don't want to change some sequence accidently we use tuples
point = (1, 2) + (3, 4)
print(point)
point1 = ("hello world")
print(point1)
X = 10
Y = 11
x, Y = Y, X
a, b = 11, 10

# Array
Numbers = array("i", [1, 2, 3])
Numbers.pop(2)
Numbers.insert(3, 5)
# creating an array with integer type
a = arr.array('i', [1, 2, 3])
# creating an array with double type
b = arr.array('d', [2.5, 3.2, 3.3])

# sets ulike list they are unordered collection we canot access item via index
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
first = set(numbers)
second = {1, 2, 5, 6}
print(uniques)
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

# dictionaries collection of key and value example phone book
point = {"X": 1, "Y": 2}

point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)
# looping over dictionary
for key, value in point.items():
    print(key, value)
# Dictionary comprehensions for below piece of code we can use list comprehension or map function
# this comprehension is not limited to list
value = []
for x in range(5):
    value.append(x*2)
#[expression for item in range(5)]
# below line of code is exactly identical as above 3 lines
# we can use with sets and dictionary
values = [x*2 for x in range(5)]
print(values)
# what is difference between syntax of sets and dictionary
# both we use curly braces but in set we use sequence and in dictionary we use key value pair
values = {x: x*2 for x in range(5)}
print(values)
# tuples will not get tuplle will get generator operator
values = (x*2 for x in range(5))
print(values)
# generator expression
# we use generator because if we have billion in range(5) so we dont want to store billion value in list so gegenrator we can use
# we can iterate over generator
values = (x*2 for x in range(5))
for x in range(10):
    print(x)
# getsizeof
values = (x*2 for x in range(100000))
print("gen:", getsizeof(values))
# comparing memory by generator and normal list
# gen: 104  List: 800984 bytes generate operator dont store all items in memory so u will
# not get the length of generator operator
#values = (x*2 for x in range(100000))
#print("List:", getsizeof(values))
# print(len(values))
# unpacking operator getting output as 1 2 3 without squere bracket and ,
numbers = [1, 2, 3]
print(numbers)
values = list(range(5))
values = [*range(5), *"Hello"]
print(values)
# combine unpacking
first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
# exercise what is most common character
sentence = "This is common interview question"

for i in sentence:
    print(i)
