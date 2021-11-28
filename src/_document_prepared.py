import _utils as ut

_doc = ['Thinking fast and Slow',
'Theories of Personality',
'WHY MEN LOVE Bitches']
_read_directory = './data/'
_out_directory = './out/'

print('Lets go =>>>>')
for _name in _doc:
    ut._convertPDFToCSV(_read_directory,_name+'.pdf' ,_out_directory,_name+'.txt' )   
    ut._cleansData(_out_directory,_name+'.txt',_out_directory,_name+'.txt')  
    print(_name + ', Done...')
