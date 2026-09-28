"Your music player's library is growing. Let's implement a set to keep track of favorite song IDs."
"Reveal the values in the array to see if 924 is in it."

start = 3 # starting address
size = 5 # size of array
mem.get_value_at(3)
mem.get_value_at(4)
mem.get_value_at(5)
mem.get_value_at(6)
mem.get_value_at(7)

"Write a specification for a function that checks if a value is in the set."

def contains(x):
    """Return True if x is in the set, or False otherwise."""
    pass 

def delete(x):
    """Remove x from the set."""
    # TODO

def insert(x):
    """Insert x into the set."""
    # TODO
# These operations define an abstract data type, or interface.

"There are a few operations we need to be able to do with our set of song IDs."
"A data structure implements an abstract data type by organizing data in memory and specifying how to perform operations."

"Program the contains operation for an array implementing a set. We've added a display function to show the result in the output title bar."

start = 6
size = 9
def contains(x):
    """Check if a song ID x is in the set"""
    for i in range(size):
        address = start + i
        if mem.get_value_at(address) == x:
            return True
    return False

display(contains(311))

"The choice of data structure affects how fast set operations are."
"The job of a data structure is to implement an interface, or abstract data type."



