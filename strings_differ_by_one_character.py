'''
Given a list of strings dict where all the strings are of the same length.

Return true if there are 2 strings that only differ by 1 character in the same index, otherwise return false.
'''

Approach 1 -- O(M^2 N)

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        seen = set()
        for word in dict: 
            for i in range(len(word)): 
                key = word[:i] + "*" + word[i+1:]
                if key in seen: return True 
                seen.add(key)
        return False
Approach 2 -- rolling hash O(MN)

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        MOD = 1_000_000_007
        hs = []
        for word in dict: 
            val = 0
            for ch in word: val = (26*val + ord(ch) - 97) % MOD
            hs.append(val)
        
        mult = 1
        for j in reversed(range(len(dict[0]))): 
            seen = {}
            for i, w in enumerate(dict): 
                val = (hs[i] - (ord(w[j]) - 97) * mult) % MOD
                if val in seen: 
                    for ww in seen[val]: 
                        if sum(x != xx for x, xx in zip(w, ww)) == 1: return True 
                seen.setdefault(val, []).append(w)
            mult = 26 * mult % MOD
        return False
-----------------------------------------------------------------------------------------
class Solution:
    def differByOne(self, array: List[str]) -> bool:
        import string
        import collections
        
        n, m = len(array), len(array[0])
        if m == 1:
            cnt = collections.Counter(array)
            return max(v for _, v in cnt.items()) > 1

        alpha = len(string.ascii_lowercase)+1
        module = 2**61 - 1 
        terminator = ord('z')-ord('a')+2
        collisions = collections.defaultdict(set)
        for word_ in array:
            word = [ord(character)-ord('a')+1 for character in word_]
            
            prefix_hash, suffix_hash = [0]*m, [0]*m
            for i in range(m):
                if i > 0:
                    prefix_hash[i] = (prefix_hash[i-1]*alpha + word[i]) % module
                else:
                    prefix_hash[i] = word[i]
            
            power = 1
            for i in range(m-1, -1, -1):
                if i < m-1:
                    suffix_hash[i] = (suffix_hash[i+1] + word[i]*power) % module
                else:
                    suffix_hash[i] = word[i]
                power *= alpha
            
            power = 1
            for i in range(m):
                hash_value = terminator*power
                if i < m-1:
                    hash_value = (hash_value + suffix_hash[i+1]) % module
                if i > 0:
                    hash_value = (prefix_hash[i-1] + hash_value) % module
                
                if hash_value in collisions:
                    for word_try in collisions[hash_value]:
                        if sum(word_[i] != word_try[i] for i in range(m)) == 1:
                            return True                    
                collisions[hash_value].add(word_)
                power *= alpha
        
        return False
For string computes prefix and suffix hashes by polynominal hash function for strings. After for all indexes concat by modulo prefix and suffix hashes and terminator addendum (for make diffirence beetween prefix and suffix hashes). If this hash value exist in collisions dictionary, check collisions naive. Collisions at average will be very low (check Rabin-Karp on wiki). Eventually time complexity is ~O(n*m)



------------------------------------------------------------------------------
class Solution:
    def differByOne(self, dictionary: List[str]) -> bool:
        dictionary = list(set(dictionary))
        hashset = set()
        count = {}
        #a:1 ~ z:26
        def order(ch):
            return ord(ch)-ord('a') + 1
        
        def add_allhash(word):
            h = set()
            m = 0 
            n = len(word)
            for i in range(n):
                m += 27**(i)*order(word[i])
            for j in range(n):
                mod = m % 27**(j)
                left = (m-mod-27**(j)*order(word[j])) 
                x = left + mod
                h.add(x)
                
            return h
        
        for w in dictionary:
            for k in add_allhash(w):
                if k in hashset:
                    return True
                hashset.add(k)
                
        return False
-------------------------------------------------------------------
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        for i in range(len(dict)):
            for j in range(i+1, len(dict)):
                cnt = 0
                for idx in range(len(dict[i])):
                    cnt += (dict[i][idx] != dict[j][idx])
                    if cnt > 1:
                        break
                if cnt == 1:
                    return True
                    
        return False
      
------------------------------------------------------------------------------------------
Idea

The brute force solution iterates through all the words and use a wildcard character (e.g. *) to replace each character. Then we throw all these wildcard strings into a hash set and check if there's any duplication.

This solution takes O(N*M^2), where N = len(dict) and M = len(dict[i]). It takes O(N) to iterate through the word list, O(M) to iterate through each character in the word, and another O(M) to create all the wildcard words.

We can use string hashing to bring down the time complexity to O(N*M). Instead of storing all the wildcard words, we store their hash value. And a wildcard word's hash value can be calculated in O(1) time. Specifically, we substract the wildcard position hash value from the word's original hash value.

Example:

hash('ba') = 2*26^1 + 1*26^0 = 53
hash('*a') = 53 - 2*26^1 = 1
hash('b*') = 53 - 1*26^0 = 52
Note that we may face hash collision problem. Here we use a large prime number (10*11 + 7) to avoid it, but there's still a chance that the algorithm fails. If we add checks for hash collision, the worst-case complexity will go back to O(N*M^2).


Complexity

Brute force:

Time complexity: O(NM^2)
Space complexity: O(NM^2)
String hashing:

Time complexity: O(NM)
Space complexity: O(NM)

Python

Brute force:

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        for j in range(m):
            seen = set()
            for i in range(n):
                new_w = dict[i][:j] + '*' +dict[i][j+1:]
                if new_w in seen:
                    return True
                seen.add(new_w)
        return False
String hashing:

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        hashes = [0] * n
        MOD = 10**11 + 7
        
        for i in range(n):
            for j in range(m):
                hashes[i] = (26 * hashes[i] + (ord(dict[i][j]) - ord('a'))) % MOD
        
        base = 1
        for j in range(m - 1, -1, -1):        
            seen = set()
            for i in range(n):
                new_h = (hashes[i] - base * (ord(dict[i][j]) - ord('a'))) % MOD
                if new_h in seen:
                    return True
                seen.add(new_h)
            base = 26 * base % MOD
        return False
      
      
