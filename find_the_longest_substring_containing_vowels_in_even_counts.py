'''
Given the string s, return the size of the longest
substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
'''

We can use 5 bits to represent the parity of the number of occurrences of vowels. For example, we can use 0/1 for even/odd numbers, then if we have 4a, 3e, 2i, 1o, 0u, the representation would be 01010. As we scan through the array, we can update the representation in O(1) time by using the XOR operation, and then store the index where every different representation first appeared. When we encounter a representation, say 01010 again at index j, we can look back on the index i where 01010 first appeared, and we know that the substring from i to j must be a valid string, and it is the longest valid substring that ends at j.

def findTheLongestSubstring(self, s: str) -> int:
    vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
    d, n, r = {0: -1}, 0, 0
    for i, c in enumerate(s):
        if c in vowels:
            n ^= vowels[c]
        if n not in d:
            d[n] = i
        else:
            r = max(r, i - d[n])
    return r
  
-----------------------------------------------------------------------------------
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def countVowels(ct):
            if not ct['a'] % 2 and not ct['e'] % 2 and not ct['i'] % 2 and not ct['o'] % 2 and not ct['u'] % 2:
                return True
            return False

        #Reducer
            #Slider
            #0 - len(s)
            #0 - len(s) -1 -> 1 - len(s)
        for i in range(len(s)):
            ctr = collections.Counter(s[:len(s) - i])
            for j in range(i+1):
                #window = s[j:(len(s)+j) - i]
                if j != 0:
                    ctr[s[j - 1]] -= 1
                    ctr[s[len(s)+j - i - 1]] += 1
                if countVowels(ctr):
                    return sum(ctr.values())
        return 0
      
-------------------------------------------------------------------
v = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
curr = 0
left = dict()
left[0] = -1
ans = 0
for index, i in enumerate(s):
	if(i in v):
		curr ^= (1<<v[i])
	if(curr not in left):
		left[curr] = index
	else:
		ans = max(ans, index - left[curr])
return ans

----------------------------------------------------------------------------------
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 16, 'e': 8, 'i': 4, 'o': 2, 'u': 1}
        vote_dict = {0: -1}
        vcount = 0
        ans = 0
        for idx, c in enumerate(s):
            if c in vowels.keys():
                vcount = vcount ^ vowels[c]
            
            if vcount in vote_dict.keys():
                ans = max(ans, idx - vote_dict[vcount])
            else:
                vote_dict[vcount] = idx
                
        return ans
