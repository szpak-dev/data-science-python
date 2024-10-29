import re
from collections import Counter

# Load and read file
with open('Data_MobyDick.txt', 'r') as file:
    text = file.read()

# Count the total number of words
words = re.findall(r'\b\w+\b', text)
total_words = len(words)
print(f"Total words: {total_words}")

# Prepare Bag of Words (case-insensitive, without punctuation)
cleaned_words = [word.lower() for word in words]
bag_of_words = Counter(cleaned_words)

print(bag_of_words)
