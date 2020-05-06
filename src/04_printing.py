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

print( 'x is %2d, y is %0.4f, z is "%s"\n' %( x, y, z))
# ...this is why I dislike modulo string formatting -- look at the float format I set


# Use the 'format' string method to print the same thing

print( "x is {2}, y is {1:.4f}, z is \"{0}\"\n".format( z, y, x))


# Finally, print the same thing using an f-string

print( f"x is {x}, y is {y:.4f}, z is \"{z}\"\n")


# ...and a bonus

values = [x, y, z]
print( *values, sep= ', ')