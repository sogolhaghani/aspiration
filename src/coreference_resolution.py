import spacy
import neuralcoref

nlp = spacy.load("en_core_web_sm")
nlp.max_length = 10300000 # or even higher

# # # Add neural coref to SpaCy's pipe

neuralcoref.add_to_pipe(nlp)

# # You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.
doc = nlp(u'My sister has a dog. She loves him.')

doc._.has_coref
print(doc._.coref_clusters)
