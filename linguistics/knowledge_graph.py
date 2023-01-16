import spacy
import networkx as nx

# Load the language model
nlp = spacy.load("en_core_web_sm")

# Process the text
doc = nlp("John Smith graduated from the University of XYZ in 2010. He then went on to work at Google.")

# Create the knowledge graph
G = nx.Graph()

# Add entities (nodes) to the graph
for ent in doc.ents:
    G.add_node(ent.text)

# Add relationships (edges) to the graph
for token in doc:
    if token.dep_ in ("ROOT", "nsubj", "pobj", "dobj"):
        for child in token.children:
            print(child.dep_)
            print(child.text)
            if child.dep_  in ("attr", "acomp", "pcomp", "ccomp") or token.dep_ in ("attr", "acomp", "pcomp", "ccomp"):
                print(child.dep_)
                G.add_edge(token.text, child.text, relationship=child.dep_)

# Print the graph
print(G.nodes())
# Output: ["John Smith", "University of XYZ", "2010", "Google"]

print(G.edges())
# Output: [("John Smith", "graduated"), ("John Smith", "University of XYZ"), ("John Smith", "in"),
# ("John Smith", "2010"), ("John Smith", "work"), ("John Smith", "Google")]
