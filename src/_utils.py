import textract
import os
import unicodedata
import re
from collections import Counter

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
                out.write(line)

    with open(_read_directory +_temp + _csv_name, 'r') as inp, open(_write_directory + _file_name, 'w') as out:    
        for line in inp:        
            line = re.sub("[\(\[].*?[\)\]]", "", line)
            out.write(line) 
    os.remove(_read_directory +_temp + _csv_name)   

# _convertPDFToCSV('../data/','3.pdf' ,'../out/','3.txt' )   
# _cleansData('../out/','3.txt','../out/','3.txt')   