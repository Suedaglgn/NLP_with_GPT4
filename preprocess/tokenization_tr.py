import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('turkish_grammar_checker')

from nltk.tokenize import word_tokenize

text = "Bu bir Türkçe örnek cümle. Birden çok kelime içerir, bunlar tokenize edilecektir."

tokens = word_tokenize(text)
print(tokens)
