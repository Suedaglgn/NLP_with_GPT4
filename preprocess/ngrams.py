def generate_ngrams_w_python(text, n):
    # Split the text into words
    words = text.split()

    # Create a list to store the n-grams
    ngrams = []

    # Iterate over the words and create the n-grams
    for i in range(len(words) - n + 1):
        ngrams.append(words[i:i + n])

    return ngrams


def generate_ngrams_w_nltk(text, n):
    from nltk.util import ngrams
    words = text.split()
    ngrams = list(ngrams(words, n))
    return ngrams


def generate_ngrams_w_textblob(text, n):
    from textblob import TextBlob

    blob = TextBlob(text)
    ngrams = blob.ngrams(n)
    return ngrams


if __name__ == '__main__':
    text = "The quick brown fox jumps over the lazy dog."

    ### python ###
    # Generate bigrams
    bigrams_w_py = generate_ngrams_w_python(text, 2)
    print(bigrams_w_py)

    # Generate trigrams
    trigrams_w_py = generate_ngrams_w_python(text, 3)
    print(trigrams_w_py)

    ### nltk ###
    # Generate bigrams
    bigrams_w_nltk = generate_ngrams_w_nltk(text, 2)
    print(bigrams_w_nltk)

    # Generate trigrams
    trigrams_w_py = generate_ngrams_w_nltk(text, 3)
    print(trigrams_w_py)

    ### textblob ###
    # Generate bigrams
    bigrams_w_tb = generate_ngrams_w_textblob(text, 2)
    print(bigrams_w_tb)

    # Generate trigrams
    trigrams_w_tb = generate_ngrams_w_textblob(text, 3)
    print(trigrams_w_tb)
