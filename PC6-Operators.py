# Operators

X = 5 + 10
print(X)


# Python Arithmetic Operators
print("\n Python Arithmetic OPerators \n")

X = 10
Y = 2
Z = 11

print(X + Y)
print(X - Y)
print(X * Y)
print(X / Y)
print(Z % Y)
print(X**Y)
print(Z // Y)

# Assignment Operators in Python
print("\n Assignment Operators \n")

x = 5

x += 2  # x = x + 2
print(x)  # Now x = 7

x -= 3  # x = 7 , x = x - 3
print(x)  # Now x = 4

x *= 5  # Now x = 4, x = x * 5
print(x)  # Now x = 20

x /= 2
print(x)

x %= 3
print(x)

x = 25
x //= 4
print(x)


x = 10
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print("\n Python identity operators\n")
x = "Apple"
y = "Apples"

print(x is y)
print(x is not y)

print("\n Python Logical Operators")
x = 5
y = 10
print(x > 2 and y > 11)
print(x > 2 and y > 6)
print(x > 2 or y > 11)
print(not (x > 2 or y > 5))


# Python Membership Operators

print("\nPython Membership operators")

a = "Apple is red"

print("Apple" in a)
print("Phone" not in a)
