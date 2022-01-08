import spacy
from spacy import displacy


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
            doc = nlp(line.strip())
            _heads = _extract_head(doc)
            _has_verb = False
            _has_obj = False
            for token in doc:
                if token.pos_ == 'VERB':
                    _has_verb = True
                if token.dep_ == 'pobj' or token.dep_ == 'dobj':
                    _has_obj = True

            # if len(_heads) == 0:
            #     print(line)
            # TODO :// remove these patern from raw text
            # if len(_heads) == 0 and len(doc) == 2:
            #     print(line)


            # TODO remove these patern from raw text
            if len(_heads) == 0 and len(doc) > 2 and _has_verb == False and _has_obj == False:
                print(line)




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
    