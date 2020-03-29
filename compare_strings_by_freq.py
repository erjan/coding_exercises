#Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

#Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

#TLE SOLUTION


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def helper(self, s):
            
            min_s = min(s)
            return s.count(min_s)
            
        
        answer = []
        for query in queries:
            c = 0
            for w in words:
                if helper(self,query) < helper(self,w):
                    c+=1
        
            answer.append(c)
        print(answer)
        return answer
    
    
    
    # i found my bug!
    #i turned queries into dictionary and this removed 1 value from actual query list.
    
   #the value removed was a repeating key in the dictionary: 'ba'

def f( queries, words):
        
    def helper( s):
            
        min_s = min(s)
        return s.count(min_s)
            
    queries_dict = dict()
    print('len of queries dict % d ' %len(queries_dict))
    for q in queries:
        queries_dict[q] = helper(q)


    print(queries)
    print(list(queries_dict.keys()))


    words_dict = dict()
    for w in words:
        words_dict[w] = helper(w)
    
    answer = []
    print('len of words dict %d ' % len(words_dict))

    q_values = list(queries_dict.values())
    w_values = list(words_dict.values())

    print('queries freqs: %s ' % q_values)
    print('words freqs: %s ' % w_values)
    print('len of queries: %d ' % len(q_values))

    print('len of words: %d ' % len(w_values))
    '''
    for q in q_values:
        #print()
        #print('-----------------------------------------------' )
        #time.sleep(0.75)
        c = 0
        for w in w_values:
            #print('comparing q %d vs word %d ' %(q, w))
            if q < w:
                #time.sleep(0.6)
                #print('found, so +1: %d < %d ' %(q,w))
                c+=1
            else:
                #print('!!!! q > w')
                #print('else %d > %d' %(q,w))
                
            #else:
                #c = len(w_values
            
        
            
        #l = list(filter(lambda x : q < x, w_values))
        #if c== 0:
         #   print('found none ')
          #  c+= len(q_values)
        #print('after: c %d, appending %d' % (c,c))
        #answer.append(c)
        
    print('len of answer %d '  % len(answer))
    print('answer')
    print(answer)
    
    expected = [6,5,0,6,11,11,11,8,11,0,6,6]
    print('expected')
    print(expected)

    print()
    print('query freqs %s' % q_values)
    print('word freqs %s' % w_values)
      '''    
    return 0

'''                         
q=["aabbabbb","abbbabaa","aabbbabaa","aabba","abb","a","ba","aa","ba","baabbbaaaa","babaa","bbbbabaa"]
w = ["b","aaaba","aaaabba","aa","aabaabab","aabbaaabbb","ababb","bbb","aabbbabb","aab","bbaaababba","baaaaa"]

q = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
w = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
'''
  
q = ["aabbabbb","abbbabaa","aabbbabaa","aabba","abb","a","ba","aa","ba","baabbbaaaa","babaa","bbbbabaa"]
w = ["b","aaaba","aaaabba","aa","aabaabab","aabbaaabbb","ababb","bbb","aabbbabb","aab","bbaaababba","baaaaa"]

f(q,w)
    
    
