"Let's build up a dictionary of word counts from a dataset."
"Complete the __init__ method to start with an empty dictionary."

class WordCounter:
    """
    Counts the number of times each word appears in the dataset.
    """
    def __init__(self):
        """Set up an empty dictionary of word:count pairs."""
        self.counts = {}

    'Let us plan a method that updates the count of a given word.'
    'What should update_count do if word is not in the dictionary?'
    def update_count(self, word):
        """Given a word from the dataset, update its count."""

    # Answer: Add the word to the dictionary and set its count to 1.

counter = WordCounter()
print(counter.counts) # {}
print() # Space

"Complete the update_count method."

class CountTheWords:
    """
    Counts the number of times each word appears in the dataset.
    """
    def __init__(self):
        """Set up an empty dictionary of word:count pairs."""
        self.counts = {}
    def update_count(self, word):
        """Given a word from the dataset, update its count."""
        if word in self.counts:
            self.counts[word] += 1 # take whatever the count is now and add 1
        else:
            self.counts[word] = 1 # set the count to 1
counter = CountTheWords()
print(counter.counts) # {}
counter.update_count("the") 
print(counter.counts) # {'the': 1}
counter.update_count("the") 
print(counter.counts) # {'the': 2}
print() # Space

"Methods that change an object's state are called mutators."
"We can use the update_count mutator to build up the object's counts dictionary."

"Make a new WordCounter instance and count all the words in the list. Print the dictionary after each word is counted."

class CountAllWordsNow:
    """
    Counts the number of times each word appears in the dataset.
    """
    def __init__(self):
        """Set up an empty dictionary of word:count pairs."""
        self.counts = {}
    def update_count(self, word):
        """Given a word from the dataset, update its count."""
        if word in self.counts:
            self.counts[word] += 1 
        else:
            self.counts[word] = 1 

word_list = ["the", "cow", "jumped", "over", "the", "moon"]
list_counter = CountAllWordsNow()
for word in word_list:
    list_counter.update_count(word)
    print(list_counter.counts)
# {'the': 1}
# {'the': 1, 'cow': 1}
# {'the': 1, 'cow': 1, 'jumped': 1}
# {'the': 1, 'cow': 1, 'jumped': 1, 'over': 1}
# {'the': 2, 'cow': 1, 'jumped': 1, 'over': 1}
# {'the': 2, 'cow': 1, 'jumped': 1, 'over': 1, 'moon': 1}

"Make another instance of the WordCounter class, and use it to count all the words in this dataset."
print() # Space
class FinalCountOfAllTheWordsYes:
    """
    Counts the number of times each word appears in the dataset.
    """
    def __init__(self):
        """Set up an empty dictionary of word:count pairs."""
        self.counts = {}
    def update_count(self, word):
        """Given a word from the dataset, update its count."""
        if word in self.counts:
            self.counts[word] += 1 
        else:
            self.counts[word] = 1 

cow_data = ( "hey diddle diddle"
    "the cat and the fiddle "
    "the cow jumped over the moon "
    "the little dog laughed "
    "to see such sport "
    "and the dish ran away with the spoon")

cow_counter = FinalCountOfAllTheWordsYes()
word_list = cow_data.split()
for word in word_list:
    cow_counter.update_count(word)
print(cow_counter.counts)

# {'hey': 1, 'diddle': 1, 'diddlethe': 1, 'cat': 1, 'and': 2, 'the': 6, 'fiddle': 1, 'cow': 1, 'jumped': 1, 'over': 1, 'moon': 1, 'little': 1, 'dog': 1, 'laughed': 1, 'to': 1, 'see': 1, 'such': 1, 'sport': 1, 'dish': 1, 'ran': 1, 'away': 1, 'with': 1, 'spoon': 1}

"You used a class to count the words in a dataset."
"Building up an instance of a class using methods is a common object-oriented technique."