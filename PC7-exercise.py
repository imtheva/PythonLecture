a = input("Enter Your Marks: ")
a = int(a)

if a >= 80 and a <= 100:
    print("You have A for the subject")
elif a >= 60 and a < 80:
    print("You have B for the subject")
elif a >= 40 and a < 60:
    print("You have C for the subject")
elif a >= 0 and a < 40:
    print("You have F for the subject")
else:
    print("Enter a valid value between 0 and 100")
