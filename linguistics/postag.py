

def posttag_w_nltk(text):
    # import nltk
    # nltk.download('punkt')
    # nltk.download('averaged_perceptron_tagger')

    from nltk.tokenize import word_tokenize
    from nltk.tag import pos_tag

    # Tokenize the text
    tokens = word_tokenize(text)

    # Part-of-speech tag the tokens
    tagged_tokens = pos_tag(tokens)

    return tagged_tokens


def posttag_w_spacy(text):

    import spacy

    # Load the spacy model
    nlp = spacy.load("en_core_web_sm")

    # Process the sentence with the spacy model
    doc = nlp(text)

    # Iterate over the tokens in the doc and print the POS tag
    for token in doc:
        print(token.text, token.pos_)


if __name__ == '__main__':
    # The text to tag
    text = "This is an example sentence. It has several words, which will be tagged with their part of speech."

    tagged_text = posttag_w_nltk(text)
    print(tagged_text)

    posttag_w_spacy(text)
