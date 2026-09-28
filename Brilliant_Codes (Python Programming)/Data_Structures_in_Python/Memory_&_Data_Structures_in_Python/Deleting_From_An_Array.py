"Even good songs can get stale after a while. Let's remove some from the set of favorites."
"Check if 442 is in the array of favorite song IDs."

start = 2 # Starting address
size = 8 # size of array
def contains(value):
    for i in range(size):
        address = start + i
        if mem.get_value_at(address) == value:
            return True
    return False

display(contains(442))

"Delete 442 from the array by clearing its memory slot. Update the size of the array."
mem.clear_value_at(9)
size -= 1

"A set interface only checks whether a value is present, so changing the order is fine."
"Delete 602 from the array, then make sure the final array doesn't have gaps or duplicate values."

start = 2
start = 7
mem.clear_value_at(6) # Can remove this to make the program perform the same task but with one fewer step.
mem.set_value_at(6, mem.get_value_at(8))
mem.clear_value_at(8)
size -= 1

"An array is a continuous chunk of memory without gaps."
"The array implements a set, which doesn't have duplicate values."

"Protip: To allow a function to modify a global variable, use the global keyword."
"Program an efficient delete operation for an array implementing a set."

start = 2
size = 6
def delete(x):
    global size
    address = start
    last = start + size - 1
    while address <= last and mem.get_value_at(address) != x:
        address += 1
    if address <= last:
        mem.set_value_at(address, mem.get_value_at(last))
        mem.clear_value_at(last)
        size -= 1

delete (924)

"Identifying and maintaining invariants helps ensure that algorithms modify data structures correctly."