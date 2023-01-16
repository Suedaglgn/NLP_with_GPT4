import spacy


def ner(text):
    # Load the pre-trained model
    nlp = spacy.load("en_core_web_sm")

    # Process the text using the model
    doc = nlp(text)

    # Iterate over the entities in the text and print their label and text
    for ent in doc.ents:
        print(ent.label_, ent.text)


if __name__ == '__main__':
    # Define the text to be processed
    text = "Apple is looking at buying U.K. startup for $1 billion"
    ner(text)
