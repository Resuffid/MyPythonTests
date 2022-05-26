print("Hello, World")

if 5 > 2:
    print("Five is greater than two!")

x = 5
y = "Hello world"

print(y, "My age is", x)

# Comment :p

# Types of variables

a = str(3)      # text
b = int(3)      # integer
c = float(3)    # real

# To check the type of variable you use command print(type(a))

print(a)
print(b)
print(c)
print(type(a))

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

Variable_I = "My name is"
print(Variable_I, " Wiktor")

# Many values
d, e, f = "Orange", "Banana", "Cherry"
print(d)
print(e)
print(f)

# Unpacking
fruits = ["apple", "banana", "cherry"]
g, h, i = fruits
print(g)
print(h)
print(i)

# Global variable

o = "awesome"

def myfunc():
  global o
  o = "fantastic"
  print("Python is", o)

myfunc()

print("Python is " + o)
