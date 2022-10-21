# For Loops Basics


city = ["Kandy", "Colombo", "Jaffna", "Galle"]

for x in city:
    print(x)

# Looping Through String
print("\n Looping Through String")

for x in "Sri Lanka":
    print(x)

# Break Statement

print("\n ")

city = [1, 15, 20, 85, 90, 48]

for x in city:

    if x == 85:
        break

    print(x)


# Continue  Statement

print("\n")
currencies = ["Dollar", "LKR", "Pounds", "LKR", "Fracks", "LKR", "Euro"]

for x in currencies:
    if x == "Pounds":
        continue

    print(x)

# Range Function

print("\n")

for x in range(10):
    print(x)


print("\n")

for x in range(500, 510):
    print(x)


print("\n")

for zinda in range(5, 50, 8):
    print(zinda)


# Else in For Loops

print("\n")

for apple in range(5, 50, 15):
    print(apple)

else:
    print("For Loop ended")


# Break statements will not execute else

print("\n")

for x in range(5, 15):
    if x == 12:
        break
    print(x)
else:
    print("Loop ended")

# Nested Loops

print("\n")

country = ["SL", "UK", "IND", "USA", "PAK"]
features = ["Currency", "Hills", "River", "Agriculture", "Sea"]

for x in country:
    for y in features:
        print(y, x)


# Pass in for loop

print("\n")

for x in [0, 1, 2]:
    pass
