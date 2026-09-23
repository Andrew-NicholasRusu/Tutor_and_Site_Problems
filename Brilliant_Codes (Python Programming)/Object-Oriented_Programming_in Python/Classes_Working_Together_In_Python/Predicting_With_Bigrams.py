"AI agents generate responses based on thousands of words of context. Let's start by trying to use just one word to predict the next word."
"In this dataset, which word most often follows 'my'?"

kitten_data = "hey my kitten my kitten and hey my kitten my deary"
# Answer: "kitten"

# Which word most often follows "kitten"?
# Answer: "my"

"A bigram model generates text by predicting the most likely next word, based on consecutive word pairs, or bigrams, in the training data."
"Since the most common next word after 'my' is 'kitten', and the most common word after 'kitten' is 'my', the model generates 'kitten' after 'my' and 'my' after 'kitten'."

"When there's a tie for the most common next word, we can pick one at random."
"Use an instance of the WordCounter class to count the words that come after 'a' and randomly choose a common word."

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

garden_data = "the bee found the flower the bee liked the garden the bird found a nest the bee found a seed"
words_after_a = ["nest", "seed"]
after_a_counter = WordCounter()
for word in words_after_a:
    after_a_counter.update_count(word)
print("I wonder if the bee found a", 
      # The loop on the first line walks through each word in words_after_a and calls update_count on the counter — so "nest" and "seed" each get a count of 1.
      # Since they're tied, random_common_word() finds both and picks one at random using randrange.
      after_a_counter. random_common_word)

"Large language models (LLMs) use a similar approach, but with massive training sets and more complex models."