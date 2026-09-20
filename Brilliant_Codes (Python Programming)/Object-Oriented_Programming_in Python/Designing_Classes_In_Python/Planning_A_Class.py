"AI agents learn by analyzing large amounts of text data. Let's build a class that helps our agent explore data by counting words."
"What is the most common word in this dataset?"

text_data = ("hey diddle diddle "
    "the cat and the fiddle"
    "the cow jumped over the moon"
    "the little dog laughed"
    "to see such sport"
    "and the dish ran away with the spoon")
# Answer : "the"

"To generate responses, an agent repeats patterns it finds in data. An important part of this process is finding common words."
"What information would be enough to find the most common word in a dataset?"
# ANswer" The number of times each word appears in the dataset.

"The first step in writing a class is planning what information it should store (its attributes) and what tasks it should be able to do (its methods)."
"The WordCounter class should store each word with its count. It should be able to update and report the count of a word."

class WordCounter:
    """
    Counts the number of times each word appears in a dataset
    """

"The WordCounter class needs to count how many times each word appears in the dataset. What's a good structure for this?"
# Answer: A dictionary of {string:number}.

"How should the class initialize its attributes?"

class CountWords:
    """
    Counts the number of times each word appears in a dataset
    """
    def __init__ (self):
        """Set up an empty dictionary of word: count pairs."""
        pass # empty for now

    "The CountWords class needs a way to count each word in the dataset."
    "What should the update_count method do?"

    def update_count(self, word):
        """Given a word from the dataset, update its count."""
        pass # Empty for now


    

