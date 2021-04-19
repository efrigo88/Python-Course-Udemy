# we're importing the whole module
#import turtle as tt

# tt.forward(150)
# tt.right(270)
# tt.forward(150)

# tt.done()

# to be more selective, we can specify in the following way
# we're solely importing the following three methods
# from turtle import forward, right, done, circle

# now, it's not necessary to use the name of the module, we can call the methods directly
# forward(150)
# right(250)
# circle(75)
# forward(150)

# done()

# another way of importing, not recommended
from turtle import *

forward(150)
right(250)
circle(75)
forward(150)

done()


