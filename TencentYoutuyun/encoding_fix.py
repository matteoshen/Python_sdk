# -*- coding: utf-8 -*-

# fixed annoying encoding problems
def basic_encoding(s):
    return s.encode('raw_unicode_escape').decode('utf8')
    
def json_encoding(j):
    '''fixed encoding issues in json
    '''
    for i in j['items']:
        i['itemstring'] = basic_encoding(i['itemstring'])
        for w in i['words']:
            w['character'] = basic_encoding(w['character'])
    return j