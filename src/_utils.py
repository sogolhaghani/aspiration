import textract
import os
import unicodedata
import re
from collections import Counter
import spacy


special_characters = "•©@#$^&*"

def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

def _convertPDFToCSV(_read_directory, _pdf_name, _write_directory, _file_name):
    text = textract.process(_read_directory + _pdf_name)
    text_file = open(_write_directory + _file_name,'w')
    text_file.write(text.decode("UTF-8"))


def _cleansData(_read_directory, _csv_name, _write_directory, _file_name):
    _temp = 'temp_'
    with open(_read_directory + _csv_name, 'r') as inp, open(_read_directory +_temp + _csv_name, 'w') as out:
        c=Counter(c.strip() for c in inp if c.strip())
        for line in c:
            line = re.sub("[\(\[].*?[\)\]]", "", line)
            token = line.split(' ')

            if line.strip() and (len(token) > 1 or (len(token) == 1 and token[len(token) - 1].endswith('.\n')) ) and c[line]==1:
                out.write(line + ' ')

    nlp = spacy.load("en_core_web_sm")
    nlp.max_length = 10300000 # or even higher
    with open(_read_directory +_temp + _csv_name, 'r') as inp, open(_write_directory + _file_name, 'w') as out:    
        for line in inp:
            doc = nlp(line)
            assert doc.has_annotation("SENT_START")
            for sent in doc.sents:
                if any(c in special_characters for c in sent.text):
                    continue
                out.write(sent.text + '\n')
    os.remove(_read_directory +_temp + _csv_name)   