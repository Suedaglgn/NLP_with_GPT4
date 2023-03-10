def distributional_semantic(sentences):

    import gensim

    # Create a dictionary of words from the sentences
    dictionary = gensim.corpora.Dictionary(sentences)

    # Create a bag-of-words representation of the sentences
    bow_corpus = [dictionary.doc2bow(sentence) for sentence in sentences]

    # Train a Latent Semantic Indexing (LSI) model on the corpus
    lsi_model = gensim.models.LsiModel(bow_corpus, id2word=dictionary, num_topics=2)

    # Print the most important words for each topic
    for topic_id, topic in lsi_model.print_topics(-1):
        print("Topic", topic_id+1, ":", topic)


def frame_semantic(sentence):
    """
    This is can not generated by GPT-4
    :return:
    """
    from frame_semantic_transformer import FrameSemanticTransformer

    frame_transformer = FrameSemanticTransformer()

    result = frame_transformer.detect_frames(sentence)

    print(f"Results found in: {result.sentence}")
    for frame in result.frames:
        print(f"FRAME: {frame.name}")
        for element in frame.frame_elements:
            print(f"{element.name}: {element.text}")


def lexical_ontology():
    """
    A lexical ontology is a structured hierarchy of words and their meanings, used to represent the relationships
    between words. Lexical ontologies are often used in natural language processing (NLP) to improve the accuracy of
    tasks such as word sense disambiguation and text classification.

    There are several libraries and tools available for building and using lexical ontologies in Python, including:

    WordNet: A lexical database of English, organized into synsets (sets of synonyms)
    pyOntology: A library for building and manipulating ontologies in Python
    Ontospy: A library for extracting and visualizing ontologies from RDF and OWL data
    :return:
    """
    import nltk
    from nltk.corpus import wordnet

    # Find synsets for the word "cat"
    synsets = wordnet.synsets("cat")

    # Print the synonyms and definitions for each synset
    for synset in synsets:
        print("Synonyms:", synset.lemma_names())
        print("Definition:", synset.definition())
        print("Hypernyms:", synset.hypernyms())
        print("Hyponyms:", synset.hyponyms())
        print("")


if __name__ == '__main__':
    # Define a list of sentences to process
    sentences = [[
        "The cat chased the mouse",
        "The dog chased the cat",
        "The mouse ran away from the cat and the dog"
    ]]
    text = "The hallway smelt of boiled cabbage and old rag mats."
    # distributional_semantic(sentences)
    # frame_semantic(text)
    lexical_ontology()
