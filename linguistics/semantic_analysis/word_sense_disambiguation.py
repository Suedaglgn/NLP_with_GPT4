"""
Word sense disambiguation (WSD)

Word sense disambiguation (WSD) is the process of determining the correct meaning of a word in a given context.
WSD is important in natural language processing (NLP) tasks because it helps to choose the correct meaning of ambiguous
words, which can have multiple meanings depending on the context in which they are used. For example, the word "bat" can
have different meanings depending on the context: it can refer to a type of mammal that flies, or it can refer to a
wooden implement used for hitting a ball. WSD helps to disambiguate these different meanings, and to choose the correct
one for a given context.

There are several approaches to WSD, including:

    Dictionary-based methods: Using a pre-defined dictionary or lexicon to determine the correct meaning of a word
    Corpus-based methods: Analyzing the context in which a word is used in a large corpus of text to determine its meaning
    Knowledge-based methods: Using external knowledge sources, such as WordNet, to disambiguate the meaning of a word

WSD is a challenging task, as it requires a deep understanding of the meaning and context of words in a natural language.
Despite these challenges, significant progress has been made in the development of WSD algorithms, and they are now
widely used in various NLP applications.

"""


def word_sense_disamibgution(word):
    # import nltk
    # nltk.download('wordnet')
    from nltk.corpus import wordnet as wn

    # Get the senses of the word
    senses = wn.synsets(word)

    # Print the senses
    for sense in senses:
        print(sense, sense.definition())


if __name__ == '__main__':
    # Define the ambiguous word and the context sentence
    word = "bat"
    word_sense_disamibgution(word)

