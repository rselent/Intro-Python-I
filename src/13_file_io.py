"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

f = open( 'foo.txt', 'r')

print( f.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

b = open( 'bar.txt', 'w')

b.write( "\nTomorrow, and tomorrow, and tomorrow, \n\
Creeps in this petty pace from day to day \n\
To the last syllable of recorded time, \n\
And all our yesterdays have lighted fools \n\
The way to dusty death. Out, out, brief candle! \n\
Life’s but a walking shadow, a poor player \n\
That struts and frets his hour upon the stage \n\
And then is heard no more: it is a tale \n\
Told by an idiot, full of sound and fury, \n\
Signifying nothing."
)

b.close()

c = open('bar.txt', 'r')
print( c.read())
