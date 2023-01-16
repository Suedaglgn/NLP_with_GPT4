import re


def clean_sentence(sentence):
    # Remove all non-alphanumeric characters
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # Convert to lowercase
    sentence = sentence.lower()

    # Remove extra whitespace
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence


if __name__ == '__main__':
    cleaned_sentence = clean_sentence("This is a sentence. It has some punctuation and capitalization.")
    print(cleaned_sentence)
