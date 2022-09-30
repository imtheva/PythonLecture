# Write a python code to get two numbers from the user and display the sum of the numbers

num1 = input("Enter the Number 1: ")
num2 = input("Enter the Number 2: ")

num1 = float(num1)
num2 = float(num2)

sum = num1 + num2

outp = "The total sum of the given numbers is: {}"

print(outp.format(sum))