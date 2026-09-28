"To store data and design data structures, we'll first need a model of computer memory."
"We've provided a MemoryBoard class to simulate how a computer's memory works. Store the value 100 in the slot at address 0."

class MemoryBoard:
    # hidden code
    def __init__(self, address, value):
        self.memory = {address: value}

    def set_value_at(self, address, value):
        """Store the value in the slot at address"""
        self.memory[address] = value

    "We've set up a memory board with values in slots 0 and 1."
    "Get the values from the first two slots, and store their sum in slot 2."
    def get_value_at(self, address):
        """Get the value from the slot at address"""
        # hidden code

mem = MemoryBoard()
mem.set_value_at(0, 100)
print() # Space

x = mem.get_value_at(0)
y = mem.get_value_at(1)
mem.set_value_at(2, x + y)
print() # Space

"Copy the value at address 5 to all the other slots."
value = mem.get_value_at(5)
for address in range(5):
    mem.set_value_at(address, value)

"Swap the values at addresses 0 and 1."
mem.set_value_at(2, mem.get_value_at(1)) # slot 2 acts as a temporary holding spot.
# you can't swap two slots by writing one into the other directly — that overwrites and loses the original value.
mem.set_value_at(1, mem.get_value_at(0))
mem.set_value_at(0, mem.get_value_at(2))
mem.clear_value_at(2)

"The word-RAM model of computation helps us think about how computers store and access data."
"In this model, computer memory is split into slots. Each slot holds a value, or word, at a specific location, or address."

"The word-RAM model of computation sets the stage for data structures."