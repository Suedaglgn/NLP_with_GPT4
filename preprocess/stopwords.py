import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords


def remove_stop_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Get the English stop words
    stop_words = stopwords.words('english')

    # Remove the stop words from the list of words
    filtered_words = [word for word in words if word not in stop_words]

    # Join the filtered words back into a single sentence
    filtered_sentence = " ".join(filtered_words)

    return filtered_sentence


if __name__ == '__main__':
    filtered_sentence = remove_stop_words("This is a sentence with stop words.")
    print(filtered_sentence)
