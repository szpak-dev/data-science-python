import re
from collections import Counter

"""
Bag of Words (BoW) is a technique used in natural language processing (NLP) and information 
retrieval to represent text data. It involves creating a "bag" of words from a text document, 
where the structure and order of words are disregarded. In this model:

1. Each document is represented as a collection (or "bag") of its unique words.
2. The frequency of each word is recorded.
3. Word order, syntax, and grammar are ignored.

For example, in the sentence "The cat sat on the mat," the bag of words representation 
might look like this:

- Words: `the`, `cat`, `sat`, `on`, `mat`
- Frequencies: `{the: 2, cat: 1, sat: 1, on: 1, mat: 1}`

The resulting BoW is often used in text classification and sentiment analysis by feeding 
word frequencies into machine learning algorithms as numerical features.
"""

with open('Data_MobyDick.txt', 'r') as file:
    text = file.read()

words = re.findall(r'\b\w+\b', text)
total_words = len(words)
print(f"Total words: {total_words}")

cleaned_words = [word.lower() for word in words]
bag_of_words = Counter(cleaned_words)

print(bag_of_words)
