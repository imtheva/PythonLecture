# If Else

# Equals: a == b
# Not Equals: a!=b
# LT: a<c
# LT or =: a<= c
# GT: a>c
# GT or =: a>=c


# IF Structure

print("Example 1\n")

a = 10
b = 12

if a == b:
    print("a = b")
else:
    print("a is not equal to b")


print("\nExample 2\n")

x = 12
y = 25

if x != y:
    print(" x not equal to y")

else:
    print("x is equal to y")

print("\nExample 3\n")

m = 25
n = 30

if m > n:
    print("m is greater than n")
else:
    print("m is less than n")


# IF Elif and Else

print("\nExample 4\n")

a = 10
b = 25

if a > b:
    print("a is greater than b")

elif a == b:
    print("a is equal to b")

else:
    print("b is greater than a")


print("\nExample 5\n")

# Distance of cities from the city D
cityA = 10
cityB = 200
cityC = 30

if cityA > cityB and cityA > cityC:
    print("City A is the longest")
elif cityB > cityA and cityB > cityC:
    print("City B is the longest")
else:
    print("City C is the longest")


print("\nExample 6\n")

a = 100
b = 20
c = 800

if a > b or a > c:
    print("At least a is greater at one place")


# Nested IF

print("\nExample 7\n")


values = 80

if values > 20:
    print("Value is greater than 20")
    if values > 50:
        print("Value is greater than 50")
        if values == 75:
            print("Value is equal to 75")
        else:
            print("Not equal to 75")



