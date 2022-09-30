# WhileLoop Basics
i = 1

while i <= 10:
    print(i)
    i = i + 1

print("\n While Loop Breaks \n")

# WhileLoops Break

i = 5

while i <= 10:
    print(i)

    if i == 8:
        break

    i = i + 1


print("\n While Loop Continue \n")

# While Loop Continues

a = 10

while a < 20:
    a = a + 1

    if a == 12:
        continue

    print(a)


print("\n While Else \n")

# While Else

i = 100

while i < 150:
    print(i)
    i = i + 1


else:
    print("The number is not less than or equal to 150")
