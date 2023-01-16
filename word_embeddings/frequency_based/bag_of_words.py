from sklearn.feature_extraction.text import CountVectorizer

# sample documents
documents = ["This is the first document.",
             "This document is the second document.",
             "And this is the third one.",
             "Is this the first document?"]

# initialize CountVectorizer class
vectorizer = CountVectorizer()

# fit and transform the documents
bag_of_words = vectorizer.fit_transform(documents)

# check the vocabulary
print(vectorizer.vocabulary_)
