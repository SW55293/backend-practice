# USELESS NO-OP
def square(x):
    x * x

# this function call makes no sense
# it's just useless computation
square(3)

# USEFUL SIDE-EFFECT (BUT IMPURE)
y = 5
def add_to_y(x):
    y += x

# this function call changes the value of y
# but it's impure, and frankly bad code
add_to_y(5)
