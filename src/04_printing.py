"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("this will return (x is 10)...hopefully!")
print("x is %d" % x)
print("this will return (y is 2.24552)...hopefully!")
print("y is %.2f" % y)
print("this will return (z is I like turtles!)...hopefully")
print("z is %s" % z)

print("YAY it worked!!!!")
# Use the 'format' string method to print the same thing
print("this will return (x is 10)...hopefully!")
print("x = {}".format(x))
print("this will return (y is 2.24552)...hopefully!")
print("y = {}".format(y))
print("this will return (z is I like turtles!)...hopefully")
print("z = {}".format(z))
print("YAY it worked!!!!")
# Finally, print the same thing using an f-string
print("this will return (x is 10)...hopefully!")
print(f'x is {x}')
print("this will return (y is 2.24552)...hopefully!")
print(f'y is {y}')
print("this will return (z is I like turtles!)...hopefully")
print(f'z is {z}')

print("YAY it worked!!!!")