import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize


def port_stemmer(text):
    # Install it if necessary
    # nltk.download('porter_test')

    from nltk.stem import PorterStemmer

    # Tokenize the text
    tokens = word_tokenize(text)

    # Initialize the stemmer
    stemmer = PorterStemmer()

    # Stem the tokens
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    print(stemmed_tokens)


def snowball_stemmer(text):
    # Install it if necessary
    # nltk.download('snowball_data')

    from nltk.stem import SnowballStemmer

    # Tokenize the text
    tokens = word_tokenize(text)

    # Initialize the stemmer
    stemmer = SnowballStemmer("english")

    # Stem the tokens
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    print(stemmed_tokens)


def turkish_stemmer(text):

    from TurkishStemmer import TurkishStemmer
    stemmer = TurkishStemmer()
    # Tokenize the text
    tokens = word_tokenize(text)

    # Stem the tokens
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    print(stemmed_tokens)


if __name__ == '__main__':

    # The text to stem
    text = "This is an example sentence. It has several words, which will be stemmed."
    port_stemmer(text)
    snowball_stemmer(text)
    turkish_stemmer(text)

