"""
## Constituency Parsing

Constituency parsing is a type of syntactic parsing that aims to represent the structure of a sentence by grouping its
words into hierarchical phrases, known as constituents. Constituency parsers are widely used in natural language
processing (NLP) tasks such as language understanding, machine translation, and text summarization.

For example, consider the following sentence: "The quick brown fox jumps over the lazy dog."

A constituency parser might produce the following parse tree for this sentence:

         S
       / | \
      /  |  \
     /   |   \
   NP   VP   NP
  / |     |   | \
 The quick  jumps  NP
             /   |   \
            over the lazy dog

In this parse tree, the words of the sentence are grouped into constituent phrases, such as the noun phrase (NP)
"The quick brown fox," and the verb phrase (VP) "jumps over the lazy dog." The root of the tree, "S," represents
the complete sentence.

Constituency parsing is one of several approaches to syntactic parsing, along with dependency parsing and other
techniques. It is commonly used in NLP because it provides a detailed and interpretable representation of sentence
structure that can be useful for a wide range of downstream tasks.
"""


def constituency_parsing_w_nltk(sentence):
    import nltk
    # nltk.download('punkt')
    # nltk.download('averaged_perceptron_tagger')
    # nltk.download('maxent_ne_chunker')
    # nltk.download('words')

    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    # Tag the tokens with part-of-speech tags
    pos_tags = nltk.pos_tag(tokens)

    # Use the NE chunker to extract named entities
    ne_chunks = nltk.ne_chunk(pos_tags)

    return ne_chunks


def constituency_parsing_w_spacy(sentence):

    import spacy

    # Load the spacy model
    nlp = spacy.load("en_core_web_sm")

    # Parse the sentence
    doc = nlp(sentence)

    # Print the parse tree
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.head.text)


"""
Dependency Parsing

Dependency parsing is a type of syntactic parsing that aims to represent the grammatical structure of a sentence by 
identifying the dependencies between its words. Dependency parsers are widely used in natural language processing (NLP) 
tasks such as language understanding, machine translation, and text summarization.

In a dependency parse, each word in a sentence is represented by a node, and the dependencies between the words are 
represented by directed edges connecting the nodes. The root node represents the main predicate of the sentence, and 
the other nodes represent the words that modify or depend on the predicate.

For example, consider the following sentence: "The quick brown fox jumps over the lazy dog."

A dependency parser might produce the following parse tree for this sentence:

     jumps
       |
      fox
     / | \
The quick brown
       |
     over
       |
      the
       |
      lazy
       |
      dog

In this parse tree, the edges represent the dependencies between the words of the sentence. For example, "fox" is the 
head of the noun phrase "The quick brown fox," and "over" is the head of the prepositional phrase "over the lazy dog."
"""


def dependency_parsing_w_nltk(sentence):
    import nltk
    # nltk.download('punkt')
    # nltk.download('averaged_perceptron_tagger')
    # nltk.download('maxent_ne_chunker')
    # nltk.download('words')
    # nltk.download('treebank')
    # wget https://nlp.stanford.edu/software/stanford-corenlp-4.2.2.zip
    # wget https://nlp.stanford.edu/software/stanford-corenlp-4.2.2-models-english.jar
    # unzip /content/stanford-corenlp-4.2.2.zip

    from nltk.parse.stanford import StanfordDependencyParser

    # Path to CoreNLP jar unzipped
    jar_path = '../stanford-corenlp-4.2.2/stanford-corenlp-4.2.2.jar'

    # Path to CoreNLP model jar
    models_jar_path = 'stanford-corenlp-4.2.2-models-english.jar'

    # Initialize StanfordDependency Parser from the path
    parser = StanfordDependencyParser(path_to_jar=jar_path, path_to_models_jar=models_jar_path)

    # Parse the sentence
    result = parser.raw_parse(sentence)
    dependency = result.__next__()
    print(dependency)


def dependency_parsing_w_spacy(sentence):

    import spacy

    # Load the spacy model
    nlp = spacy.load("en_core_web_sm")

    # Parse the sentence
    doc = nlp(sentence)

    # Print the dependency parse
    for token in doc:
        print(token.text, token.dep_, token.head.text)


if __name__ == '__main__':

    # Define the sentence to parse
    sentence = "The quick brown fox jumps over the lazy dog."

    # print(constituency_parsing(sentence))

    constituency_parsing_w_spacy(sentence)

