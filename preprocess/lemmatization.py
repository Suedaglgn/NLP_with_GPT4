import nltk
# nltk.download('punkt')
# nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return "a"
    elif treebank_tag.startswith('V'):
        return "v"
    elif treebank_tag.startswith('N'):
        return "n"
    elif treebank_tag.startswith('R'):
        return "r"
    else:
        print(treebank_tag)
        return " "


def lemmatize(text):

    # Tokenize the text
    tokens = word_tokenize(text)

    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Lemmatize the tokens
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    print(lemmatized_tokens)


if __name__ == '__main__':
    # The text to lemmatize
    text = "This is an example sentence. It has several words, which will be lemmatized."

    lemmatize(text)
