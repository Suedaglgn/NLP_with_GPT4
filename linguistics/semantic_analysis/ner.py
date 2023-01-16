"""
Name Entity Recognition NER

Named entity recognition (NER) is the task of identifying and labeling named entities in a text. Named entities are
specific people, organizations, locations, dates, and so on, that can be identified and labeled uniquely. NER is an
important task in natural language processing (NLP) because it allows computers to extract structured information from
unstructured text, and to understand the relationships between named entities and the surrounding text.

For example, consider the following sentence: "Apple is looking to buy U.K. startup for $1 billion." In this sentence,
the named entities are "Apple", "U.K.", and "$1 billion". NER systems can recognize these named entities and label them
appropriately, such as "Organization", "Location", and "Money".

There are several approaches to NER, including:

    Rule-based systems: Using a set of pre-defined rules to identify and label named entities
    Dictionary-based systems: Using a pre-defined dictionary or lexicon of named entities to identify and label them
    Machine learning-based systems: Training a machine learning model on a labeled dataset of named entities to
    recognize and label them in new text

NER is a challenging task, as named entities can vary greatly in terms of their spelling, formatting, and context.
Despite these challenges, significant progress has been made in the development of NER systems, and they are now widely
used in a variety of NLP applications.
"""


def ner_w_nltk(sentence):
    import nltk
    nltk.download('maxent_ne_chunker')
    nltk.download('words')

    from nltk import word_tokenize, pos_tag, ne_chunk

    # Tokenize and POS tag the words in the sentence
    words = word_tokenize(sentence)
    print(words)
    tags = pos_tag(words)
    print(tags)
    # Use the ne_chunk function to extract the named entities
    named_entities = ne_chunk(tags)

    # Print the named entities
    for entity in named_entities:
        if hasattr(entity, 'label'):
            print(entity.label(), ' '.join(word for word, tag in entity))


def ner_w_spacy(sentence):
    # python -m spacy download en_core_web_sm

    import spacy

    # Load the spacy model
    nlp = spacy.load("en_core_web_sm")

    # Process the sentence with the spacy model
    doc = nlp(sentence)

    # Iterate over the entities in the document and print their label and text
    for ent in doc.ents:
        print(ent.label_, ent.text)


if __name__ == '__main__':
    sentence =  "Apple is looking to buy U.K. startup for $1 billion"
    ner_w_spacy(sentence)

