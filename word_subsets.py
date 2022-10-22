'''
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.
'''

#bad code

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        
        
        w1 = Counter(words1)
        w2 = Counter(words2)
        
        res = []
        
        for i in range(len(words1)):
            
            curw1 = words1[i]
            curw1_counter = Counter(curw1)
            flag = True
            word_to_check = None
            for j in range(len(words2)):

                curw2 = words2[j]

                curw2_counter = Counter(curw2)
                word_to_check = curw2
                if list(curw2_counter.values()) != list(curw1_counter.values()):
                    flag = False
            
            if flag:
                res.append(word_to_check)
        return res
            
            
--------------------------------------------------------------------------------------------------           
            
            

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = set(words1)
        letters = {}
        for i in words2:
            for j in i:
                count = i.count(j)
                if j not in letters or count > letters[j]:
                    letters[j] = count
        for i in words1:
            for j in letters:
                if i.count(j) < letters[j]:
                    ans.remove(i)
                    break
        return list(ans)
-----------------------------------------------------------------------------------------
Now, that we understand the concepts involved and have better understanding of the solution. Let's look at ways to solve that,

Brute force [Time Limit Exceeded]
The trivial way to solve the problem can be described with following steps,

result = []
for every word a in A
for every word b in B check if that's subset of B
if true, then a is universal word
Add a to result
return result
Below is the simple python implementation for above algorithm,

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
            
        counters = defaultdict(dict)
        
        # put all word feq maps in counters
        for word_a in A:
            counters[word_a] = Counter(word_a)
        
        for word_b in B:
            counters[word_b] = Counter(word_b)
        
        def isSubset(a, b) -> bool: # check if b is subset of a
            counter_a = counters[a]
            counter_b = counters[b]
            
            # if counter_b has more keys then it can't be subset of a
            if len(counter_b.keys()) > len(counter_a.keys()):
                return False
            
            # can't be subset if any key in counter_b is not present in counter_a
            # or if the freq doesn't match
            for key in counter_b.keys():
                if (key not in counter_a.keys()) or (counter_a[key] < counter_b[key]):
                    return False
                
            # that means word b is subset of word a
            return True
        
        result = []
        
        for word_a in A:
            universal = True
            for word_b in B:
                if not isSubset(word_a,word_b):
                    universal = False
                    break
            if universal:
                result.append(word_a)
                
        return result




















