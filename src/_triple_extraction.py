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
            doc = nlp(line)
            _heads = _extract_head(doc)
            if len(_heads) == 0:
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
    