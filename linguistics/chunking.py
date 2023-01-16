import nltk
from nltk.chunk import RegexpParser


def chunking(sentence):
    # Define a grammar for chunking
    grammar = r"""
        NP: {<DT|JJ|NN.*>+}
        PP: {<IN|TO>}
        VP: {<VB.*>}
    """
    chunk_parser = RegexpParser(grammar)

    # Tokenize a sample sentence
    tokens = nltk.word_tokenize(sentence)

    # POS tag the tokenized sentence
    tagged_tokens = nltk.pos_tag(tokens)

    # Perform chunking
    chunked_sentence = chunk_parser.parse(tagged_tokens)
    print(chunked_sentence)


if __name__ == '__main__':
    sentence = "The quick brown fox jumps over the lazy dog"
    chunking(sentence)
