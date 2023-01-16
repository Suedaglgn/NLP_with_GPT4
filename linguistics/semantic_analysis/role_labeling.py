"""
Semantic Role Labeling (SRL)
Semantic role labeling (SRL) is the task of identifying the arguments of a predicate (a verb or verb phrase) in a
sentence, and labeling them with their corresponding semantic roles. Semantic roles indicate the underlying meaning and
purpose of a word in a sentence, and they can help to understand the relationships and interactions between the words
in the sentence.

For example, consider the following sentence: "The cat chased the mouse." In this sentence, "cat" and "mouse" are the
arguments of the predicate "chased", and they have the semantic roles of "agent" (the entity performing the action) and
"patient" (the entity affected by the action), respectively.

There are several approaches to SRL, including:

    Rule-based systems: Using a set of pre-defined rules to identify and label the arguments of a predicate
    Machine learning-based systems: Training a machine learning model on a labeled dataset of predicates and arguments
    to recognize and label them in new text

SRL is an important task in natural language processing (NLP) because it allows computers to extract structured
information from unstructured text, and to understand the relationships between the words in a sentence.
"""


def srl_w_spacy(sentence):

    import spacy

    # Load the spacy model
    nlp = spacy.load("en_core_web_sm")

    # Process the sentence with the spacy model
    doc = nlp(sentence)

    # Find the main verb in the sentence
    verb = [token for token in doc if token.pos_ == "VERB"][0]

    # Print the arguments of the verb and their semantic roles
    for arg in verb.children:
        print(arg.text, arg.dep_)


if __name__ == '__main__':
    # Define the sentence to process
    sentence = "The cat chased the mouse"
    srl_w_spacy(sentence)
