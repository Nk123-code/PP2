# Example 1

x = 5
y = "John"
print(x)
print(y)

# Example 2

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Example 3

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Example 4

x = 5
y = "John"
print(type(x))
print(type(y))

'''
Output:
    <class 'int'>
    <class 'str'>
'''

# Example 5

x = "John"
 # is the same as
x = 'John'

# Example 6

a = 4
A = "Sally"
#A will not overwrite a

# Example 7

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Example 8

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Example 9

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Example 10

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Example 11

x = "Python is awesome"
print(x)

# Example 12

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Example 13

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Example 14

x = 5
y = 10
print(x + y)

# Example 15

x = 5
y = "John"
print(x, y)

# Example 16

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Example 17

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Example 18

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# Example 19

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

