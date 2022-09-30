# Strings

a = "Hello"
b = 'Hello'

# Assign string to a variable
print("\nSingle Line String Assignment")
a = "Hello World!"
print(a)

print("\nMulti Line String Assignment")
a = """Multiline sentencee
words assignement"""
print(a)

print("\nMulti Line String Assignment")
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

print("\nCharacter position in strings")
a = "Hello, World!"
print(a[1])

print("\nLooping Through a string")
for x in "Hello World!":
    print(x)


print("\nString Length")
a = "Hello, World!"
print(len(a))

print("\nCheck if and if not")

txt = "The best things in life are free!"
print("Free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

print("\nSlice Strings")
b = "Hello, World!"
print(b[1:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])


b = "Hello, World!"
print(b[-5:-2])


print("\nModifiy Strings")
a = "Hello, World!"
print(a.upper())
print(a.lower())

a = " Hello, World! "
print(a.strip())  # returns "Hello, World!


a = "Hello, World!"
print(a.replace("H", "J"))


a = "Hello, World!"
print(a.split(","))


print("\nString Concatenation")
a = "Hello"
b = "World"
c = a + b
print(c)


a = "Hello"
b = "World"
c = a + " " + b
print(c)

print("\nString Formatting")
age = 50
txt = "My name is Kumar, and I am {}"
print(txt.format(age))


quantity = 10
itemno = 899
price = 1299
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


txt = 'We are the so-called "Vikings" from the north.'
print(txt)


