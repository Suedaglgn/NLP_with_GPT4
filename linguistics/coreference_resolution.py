"""
virtualenv --python="/usr/bin/python3.7" "/virenv/nlp3.7"
pip install neuralcoref
pip uninstall spacy
pip install spacy==2.1.0
python3 -m spacy download en
nano coref.py
fill the file with code below
python3 coref.py
"""


import spacy
nlp = spacy.load('en')
import neuralcoref
coref = neuralcoref.NeuralCoref(nlp.vocab)
# nlp = spacy.load('en')
nlp.add_pipe(coref, name='neuralcoref')
# You're done. You can now use NeuralCoref the same way you usually manipulate a SpaCy document and it's annotations.
doc = nlp('My sister has a dog. She loves him.')
print(doc._.has_coref)
print(doc._.coref_clusters)
print(doc._.coref_resolved)
