# pip install spacy-dbpedia-spotlight

import spacy_dbpedia_spotlight

nlp = spacy_dbpedia_spotlight.create('en')

doc = nlp('The president of USA is calling Boris Johnson to decide what to do about coronavirus')
print("Entities", [(ent.text, ent.label_, ent.kb_id_) for ent in doc.ents])

### OUTPUT ###
"""
Entities [('USA', 'DBPEDIA_ENT', 'http://dbpedia.org/resource/United_States'), 
('Boris Johnson', 'DBPEDIA_ENT', 'http://dbpedia.org/resource/Boris_Johnson'), 
('coronavirus', 'DBPEDIA_ENT', 'http://dbpedia.org/resource/Coronavirus')]
"""
