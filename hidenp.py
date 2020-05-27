'''
Write a function named hidenp that takes two strings and returns 1
if the first string is hidden in the second one,
otherwise returns 0 followed by a newline.

Let s1 and s2 be strings. We say that s1 is hidden in s2 if it's possible to
find each character from s1 in s2, in the same order as they appear in s1.
Also, the empty string is hidden in any string
'''


def f(s1,s2):
    start = 0
    indexes = list()
    res = []

    if len(s1) == 0:
        return True
    if len(s2) == 0:
        return False
    for i in range(len(s1)):
         
        for j in range(start, len(s2)):
            #print('starting from index start: %d' % start)
            if s1[i] == s2[j]:
                #print("found at %d " % j)
                indexes.append(j)
                res.append(s2[j])
                start = j+1
                break

            
    print('indexes')
    print(indexes)
    res = ''.join(res)
    print(res)
    if len(res) != len(s1):
        print('bad')
        return False
    elif res == s1:
        print('good')
        return True
   
                



s1 = "fgex.;"
s2 = "tyf34gdgf;'ektufjhgdgex.;.;rtjynur6"

#s1 = 'abc'
#s2 = 'btarc'


#s1 = ''
#s2 = 'long string ?ddl'

#s1 = 'abcd'
#s2 = 'b'



f(s1,s2)
