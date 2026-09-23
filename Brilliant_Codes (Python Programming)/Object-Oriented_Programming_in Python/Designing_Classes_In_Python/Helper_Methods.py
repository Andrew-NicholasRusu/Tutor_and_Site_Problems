"Let's generate common words based on a dataset."
"Use an instance of WordCounter to find the number of distinct words in this dataset."

from random import randrange
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
    def get_count(self, word):
        """
        Return the number of times a word appears in the dataset.
        """
        return self.counts.get(word, 0)
    def in_dataset(self, word):
        """Return whether a word is in the dataset."""
        return word in self.counts
    def distinct_words(self):
        """Return the number of distinct words is the dataset."""
        return len(self.counts)
    def total_words(self):
        """Return the total number of words in the dataset."""
        total = 0
        for word in self.counts:
            total += self.counts[word]
        return total
    
    "Since counting all the words in a dataset is a common task, let's make it into a class method."
    "Complete the count_data method and use it to count all the words in the dataset."

    def count_data(self, text):
        """Count all the words in a text string."""
        words = text.split()
        for word in words:
            self.update_count(word) # The count_data method calls the update_count method to count each word in the text.

    "AI agents generate responses by predicting the most likely words. A first step is finding common words in data."
    "Write a method that returns the greatest value of any word count."

    def greatest_count(self):
        """Return the highest word count in the dataset."""
        greatest = 0
        for word in self.counts:
            word_count = self.get_count(word)
            if word_count > greatest:
                greatest = word_count
        return greatest

    "Sometimes multiple words might be tied for the highest word count."
    "Write a method that returns a list of all the words with the highest word count."

    def most_common_words(self):
        """Return a list of the most common words."""
        most_common = []
        max_count = self.greatest_count()
        for word in self.counts:
            word_count = self.get_count(word)
            if word_count == max_count:
                most_common.append(word)
        return most_common

    "Protip: The randrange(n) function returns a random number in the range from 0 to n−1. Let's import it."
    "Write a method that returns one of the most common words at random. Use it to generate 10 random common words."

    def random_common_word(self):
        """Return one of the most common words at random."""
        common_list = self.most_common_words()
        choice = randrange(len(common_list))
        return common_list[choice]

pickle_data = (
    "Peter Piper picked a peck of pickled peppers"
        "a peck of pickled peppers Peter Piper picked"
        "if Peter Piper picked a peck of pickled peppers"
        "where's the peck of pickled peppers Peter Piper picked"
)
pickle_counter = WordCounter()
words = pickle_data.split()
for word in words:
    pickle_counter.update_count(word)
print("Distinct words:", pickle_counter.distinct_words()) # Distinct words: 11
print() # Space

pickle_counter.count_data(pickle_data)
print(pickle_counter.counts) # {'Peter': 8, 'Piper': 8, 'picked': 6, 'a': 4, 'peck': 8, 'of': 8, 'pickled': 8, 'peppersa': 2, 'peppers': 4, 'pickedif': 2, "pepperswhere's": 2, 'the': 2}
print() # Space

pickle_counter.count_data(pickle_data)
print("Greatest count:", pickle_counter.greatest_count()) # Greatest count: 12
print() # Space

print("Most common words:")
print(pickle_counter.most_common_words()) 
# Most common words:
# ['Peter', 'Piper', 'peck', 'of', 'pickled']
print() # Space

for i in range(10):
    print(pickle_counter.random_common_word())

# peck
# pickled
# peck
# pickled
# peck
# Peter
# Piper
# peck
# of
# Peter

"A method can call another method as a helper."
"Since the methods of a class perform related tasks, one method will often depend on another."
