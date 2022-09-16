'''
You are given an array of strings of the same length words.

In one move, you can swap any two even indexed characters or any two odd indexed characters of a string words[i].

Two strings words[i] and words[j] are special-equivalent if after any number of moves, words[i] == words[j].

For example, words[i] = "zzxy" and words[j] = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz".
A group of special-equivalent strings from words is a non-empty subset of words such that:

Every pair of strings in the group are special equivalent, and
The group is the largest size possible (i.e., there is not a string words[i] not in the group such that words[i] is special-equivalent to every string in the group).
Return the number of groups of special-equivalent strings from words.
'''

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = set()
        for s in A:
            sort_odd_even = ''.join(sorted(s[1::2]) + sorted(s[::2]))
            res.add(sort_odd_even)
        return len(res)
      
      
      
----------------------------------------------------------------------
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        l=[]
        for s in A:
            even=""
            odd=""
            for i in range(len(s)):
                if i%2!=0:
                    odd+=s[i]
                    
                else:
                    even+=s[i]
                    
            odd = ''.join(sorted(odd))
            even = ''.join(sorted(even)) 
            # odd=sorted(odd)
            # even=sorted(even)
            
            l.append(str(odd)+str(even))
            
        # print(l)    
            
        return len(set(l))     
-----------------------------------------------      
      
