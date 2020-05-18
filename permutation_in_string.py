#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
#In other words, one of the first string's permutations is the substring of the second string.


def f(s1, s2):
    print('s2 is ' + s2)
    s1_sorted = ''.join(sorted(s1))
    for i in range(0,len(s2)):
        sub = s2[i: i + len(s1)]
        sub_sorted = ''.join(sorted(sub))
        if len(sub_sorted) == len(s1):

            print('the substring is ' + sub + ', and its sorted ' + sub_sorted)
            if sub_sorted == s1_sorted:
                print('found, gtfo out!')
                return True
    print('not found')
    return False
            



s2 = 'eidbaooo'
#s2 = 'eidboaoo'
s1 = 'ab'

#s1 = 'acd'
#s2 = 'dcda'

print(f(s1,s2))



    
        
