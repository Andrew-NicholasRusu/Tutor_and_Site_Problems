"Let's plan a class that can generate text based on bigrams."
"Choose the next three words that a bigram model trained on texting_data is most likely to generate."

texting_data = (
    "hey want to see a movie "
    "sure i can meet you there "
    "ok cool see you soon "
    "she want see you also "
    "wait are you there"
)

#  she is going to see you there

"Let's plan some attributes and methods for a BigramModel class."
"In order for the BigramModel class to generate the most likely follower of each word, what information does it need to store?"

class BigramModel:
    """Predicts the next word based on word pair patterns."""
    # ...

# Answer: For each word in the training dataset, the counts of all the words that follow it.

"How could the BigramModel class use the WordCounter class to keep track of all the words that come after each word in the training dataset?"

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
        """Return the number of distinct words in the dataset.
        """
        return len(self.counts)
    def total_words(self):
        """Return the total number of word in the dataset."""
        total = 0
        for word in self.counts:
            total += self.counts[word]
        return total 
    def count_data(self, text):
        """Count all the words in a text string."""
        words = text.split()
        for word in words:
            self.update_count(word)
    def greatest_count(self):
        """Return the highest word count in the dataset."""
        greatest = 0
        for word in self.counts:
            word_count = self.get_count(word)
            if word_count > greatest:
                greatest = word_count
        return greatest
    def most_common_words(self):
        """Return a list of the most common words."""
        most_common = []
        max_count = self.greatest_count()
        for word in self.counts:
            word_count = self.get_count(word)
            if word_count == max_count:
                self.most_common_words(word)
        return most_common
    def random_common_word(self):
        """Return one of the most common words at random."""
        common_list = self.most_common_words()
        choice = randrange(len(common_list))
        return common_list[choice]
    class NewBigramModel:
        """Predicts the next word based on word pair patterns."""

# Answer: For each word in the dataset, store a separate WordCounter instance to count the words that come after it.

        "How should the NewBigramModel class initialize its data?"
        def __init__(self):
            """Set up an empty dictionary of word : WordCounter pairs."""
            pass # Empty for now

        "The BigramModel needs a way to learn, or be trained, from text data."
        "Given a text dataset as input, what should the train method do?" 
        def train(self, text):
            """For each word in the training dataset, build a WordCounter instance using all the words that follow it."""
            pass # Empty for now.

        "Bigram models typically vary their word choices. For our version, let's choose randomly if there's a tie for the most common next word."
        "Given a word as input, what should the predict_next method do?"
        def predict_next(self, word):
            """Given a word, return its most common next word, breaking ties randomly."""
            pass # Empty for now

        def generate(self, start, length):
            """Given a starting word, and length, generate text by chaining predictions."""
            pass # Empty for now

"You planned a class for generating text based on bigram patterns."
"Planning how classes work together is a key part of object-oriented design."