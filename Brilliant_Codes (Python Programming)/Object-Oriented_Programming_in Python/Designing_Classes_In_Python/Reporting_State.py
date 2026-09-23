"Now that we can build up state in our counter, let's write some methods to access it."
"Create a new WordCounter instance, and count all the words in the dataset."

class WordCounter:
    """
    Counts the number of times each word appears in a dataset.
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
    "Let's write a method that returns the correct count for a word, and returns 0 when the word is not in the dataset."
    "Complete the get_count method."
    def get_count(self, word):
        """
        Return the number of times a word appears in the dataset.
        """
        if word in self.counts:
            return self.counts[word]
        else:
            return 0
        "Protip: Dictionaries have a built-in get method that returns a default value for keys not in the dictionary. "
        # return self.counts.get(word, 0)

    "Write a method that returns whether a word is in the dataset."
    def in_dataset(self, word):
        """Return whether a word is in the dataset."""
        return word in self.counts

    "Write methods to return the number of distinct words in the dataset and the total number of words."
    def distinct_words(self):
        """Return the number of distinct words is the dataset."""
        return len(self.counts)
    def total_words(self):
        """Return the total number of words in the dataset."""
        total = 0
        for word in self.counts:
            total += self.counts[word]
        return total
        
# count all words in dataset
sea_data = ( "if all the seas were one sea "
    "what a great sea that would be "
    "and if all the trees were one tree "
    "what a great tree that would be "
    "and if all the axes were one axe "
    "what a great axe that would be "
    "and if all the men were one man "
    "what a great man he would be "
    "and if the great man took the great axe "
    "and cut down the great tree "
    "and let it fall into the great sea "
    "what a splish splash that would be"
)
sea_counter = WordCounter()
words = sea_data.split()
for word in words:
    sea_counter.update_count(word)
print(sea_counter.counts)
# {'if': 5, 'all': 4, 'the': 8, 'seas': 1, 'were': 4, 'one': 4, 'sea': 3, 'what': 5, 'a': 5, 'great':8, 'that': 4, 'would': 5, 'be': 5, 'and': 6, 'trees': 1, 'tree': 3, 'axes': 1, 'axe': 3, 'men': 1, 'man': 3, 'he': 1, 'took': 1, 'cut': 1, 'down': 1, 'let': 1, 'it': 1, 'fall': 1, 'into': 1, 'splish': 1, 'splash': 1}
print() # Space

print("Count of 'sea' =", sea_counter.get_count("sea")) # Count of 'sea' = 3
print("Count of 'ocean' =", sea_counter.get_count("ocean")) # Count of 'ocean' = 0
print() # Space

print("'take' in dataset:", sea_counter.in_dataset("take")) # 'take' in dataset: False
print("'took' in dataset:", sea_counter.in_dataset("took")) # 'took' in dataset: True
print() # Space

print("Distinct words:", sea_counter.distinct_words()) # Distinct words: 30
print("Total words:", sea_counter.total_words()) # Total words: 89

"Methods that report values but don't change the state are called accessors."
"Given a word as input, the get_count method returns the number of times it appears in the dataset."
"Using methods to report properties of an object helps make code easier to read and interpret."

