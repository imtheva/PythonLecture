# 1.1 Assigning Values to Variables

counter = 1000
miles = 1000.0
name = "My name is Vikram"

print(counter)
print(miles)
print(name)

# 1.2 Data types

print("\nData Types in python")

x = "Hello World"  # String
print(x)

x = 20  # integer
print(x)

x = 20.5  # float
print(x)

x = 1j  # complex
print(x)

x = ["apple", "banana", "cherry"]  # list
print(x)

x = ("apple", "banana", "cherry")  # tuple
print(x)

x = range(6)  # Range
print(x)

x = {"name": "John", "age": 36}  # Dict
print(x)

x = {"apple", "banana", "cherry"}  # set
print(x)

x = frozenset({"apple", "banana", "cherry"})  # frozenset
print(x)

x = True  # boolean
print(x)

x = b"Hello"  # bytes
print(x)

x = bytearray(5)  # bytearray
print(x)

x = memoryview(bytes(5))  # memoryview
print(x)

x = None  # NoneType
print(x)


# 1.3 Multiple Assignment

print("\nMultiple assignments in python")

a = b = c = 10
print(a)
print(b)
print(c)

a, b, c = 1, 2.5, "john"
print(a)
print(b)
print(c)


# 1.4 Casting the data type

print("\nCasting the data type in python")

x = int(3)
y = float(3)
z = str(3)
print(x)
print(y)
print(z)


# 1.5 Get the data type

print("\nPrinting the data types")

x = 5
y = "John"
print(type(x))
print(type(y))


# 1.6 Case-Sensitive of data type

print("\nChecking the Case sensitivity of the data types")

a = 4
A = "Sally"
print(a)


# 1.7 Variable Names

# Legal variable names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegeal Variable names

# 2myvar = "John"
# my-var = "John"
# my var = "John"


# 1.8 Multi Words Variable Names

myVariableName = "John"  # Camel Case
MyVariableName = "John"  # Pascal Case
my_variable_name = "John"  # Snake Case


# 1.9 Unpack a collection

print("\nUnpack a collection")

Fruits = ["Mango", "Jackfruit", "Banana"]

x, y, z = Fruits
print(x)
print(y)
print(z)
