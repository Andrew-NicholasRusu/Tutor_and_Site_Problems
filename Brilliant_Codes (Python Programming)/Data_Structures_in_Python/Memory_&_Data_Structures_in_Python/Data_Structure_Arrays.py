"Let's build the storage system for a custom music player. It stores favorite songs using numeric IDs."
"Store the song IDs 771, 350, 195, and 643 in the array, starting at memory address 2."

mem.set_value_at(2, 771)
mem.set_value_at(2, 350)
mem.set_value_at(4, 195)
mem.set_value_at(5, 643)

"A data structure is a concrete way to organize data in memory. An array occupies one continuous chunk of memory."
"To build an array, the computer’s memory manager has to find a block of free memory addresses and allocate them to the array."

"The alloc(x) method returns the starting address of a free chunk of size x. Use it to get the starting address for an array to store the items in id_list."

id_list = [297, 961, 185, 302, 544, 821, 438]
address = mem.alloclen(id_list)

"Write a build function that builds an array to store all the song IDs."

def build(values):
    address = mem.alloc(len(values))
    for value in values:
        mem.set_value_at(address, value)
        address += 1

song_ids = [297, 961, 185, 302, 544, 821, 438]
build(song_ids)

"Every data structure comes with code specifying how to do operations like build."