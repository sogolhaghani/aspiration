import spacy
from spacy import displacy
# import re

from collections import Counter


def _extract_head(doc):
    _sub = []
    for chunk in doc.noun_chunks:
        if chunk.root.dep_ == 'nsubj' or chunk.root.dep_ == 'nsubjpass':
            _sub.append(chunk.text)
    return _sub


def _extract_triple(_read_directory, _csv_name, _write_directory, _file_name):
    nlp = spacy.load("en_core_web_sm")
    nlp.max_length = 3030000 
    with open(_read_directory + _csv_name, 'r') as inp:
        for line in inp:
            # counts=Counter(line)
            # if counts['.']>1:
            #     print(line)
            doc = nlp(line.strip())
            _heads = _extract_head(doc)
            # _has_verb = False
            # _has_obj = False
            # _ner_num = 0 
            # for token in doc:
            #     if token.pos_ == 'VERB':
            #         _has_verb = True
            #     if token.dep_ == 'pobj' or token.dep_ == 'dobj':
            #         _has_obj = True
            # for ent in doc.ents:
            #     _ner_num +=1  

            # if len(_heads) == 0:
            #     print(line)
            # TODO :// remove these patern from raw text
            if len(_heads) == 0 and len(doc) <= 2:
                print(line)


            # TODO remove these patern from raw text
            # if len(_heads) == 0 and len(doc) > 2 and _has_verb == False and _has_obj == False:
            #     print(line)

            # if len(_heads) == 0 and len(doc) > 2 and _has_verb == True and _has_obj == False and _ner_num == 0:
            #     print(line)  
            # if len(_heads) > 0 and _ner_num > 1 and _has_verb == False:
            #     print(line)

            # TODO :// replace cite
            # pattern = r'\(([^"\)]*|\bAnonymous\b|"[^"\)]*")(, )([\d]+|n\.d\.|[\d]+[\w])\)'
            # pattern = r'^(?:[a-zA-Z]\.|[0-9]\.)+$'
            # results = re.finditer(pattern, line.strip())
            # for match in results:
            #     print(match)
            #     print(line)
            #     break





_doc = [
    # 'Thinking fast and Slow',
    'Theories of Personality'
    # 'WHY MEN LOVE Bitches'
]
_read_directory = './data/'
_out_directory = './out/'

print('Lets go =>>>>')
for _name in _doc:
    _extract_triple(_out_directory,_name+'.txt',_out_directory,_name+'.txt')  
    