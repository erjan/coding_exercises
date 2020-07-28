'''

quick lambda-in-lambda example of flattening lists
'''

from collections import OrderedDict


def make_distinct(el):
    result = ''.join(list(OrderedDict.fromkeys(el)))
    return result



d = ['STTTAAAACCKKKK', 'OOOVVVER']

result = ' '.join(list(map( make_distinct , d)))

print(result)


result2 = ' '.join(list(map( lambda el: ''.join(list(dict.fromkeys(el))), d)))

print(result2)
    
