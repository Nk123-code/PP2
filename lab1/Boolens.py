# Example 1
print(10 > 9)#true
print(10 == 9)#false
print(10 < 9)#false

# Example 2

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Example 3

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Example 4

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Example 5

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Example 6

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Example 7
x = 200
print(isinstance(x, int))
