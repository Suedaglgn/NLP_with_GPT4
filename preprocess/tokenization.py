import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

# The text to tokenize
text = "This is an example sentence. It has several words, which will be tokenized."

# Tokenize the text
tokens = word_tokenize(text)

print(tokens)