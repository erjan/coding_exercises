'''
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]
'''


We can solve this problem by mapping each string in strings to a key in a hashmap. We then return hashmap.values().

{
     (1, 1): ['abc', 'bcd', 'xyz'],  
  (2, 2, 1): ['acef'],   
      (25,): ['az', 'ba'],   
         (): ['a', 'z']
}
The key can be represented as a tuple of the "differences" between adjacent characters. Characters map to integers (e.g. ord('a') = 97). For example, 'abc' maps to (1,1) because ord('b') - ord('a') = 1 and ord('c') - ord('b') = 1
We need to watch out for the "wraparound" case - for example, 'az' and 'ba' should map to the same "shift group" as a + 1 = b and z + 1 = a. Given the above point, the respective tuples would be (25,) (122 - 97) and (-1,) (79 - 80) and az and ba would map to different groups. This is incorrect.
To account for this case, we add 26 to the difference between letters (smallest difference possible is -25, za) and mod by 26. So, (26 + 122 - 97) % 26 and (26 + 79 - 80) % 26 both equal (25,)
def groupStrings(self, strings: List[str]) -> List[List[str]]:
	hashmap = {}
	for s in strings:
		key = ()
		for i in range(len(s) - 1):
			circular_difference = 26 + ord(s[i+1]) - ord(s[i])
			key += (circular_difference % 26,)
		hashmap[key] = hashmap.get(key, []) + [s]
	return list(hashmap.values())
Time complexity would be O(ab) where a is the total number of strings and b is the length of the longest string in strings.
Space complexity would be O(n), as the most space we would use is the space required for strings and the keys of our hashmap.

--------------------------------------------------------------------------

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ## RC ##
        ## APPROACH : GREEDY ##
        ## LOGIC ##
        ## 1. Intuition is: there will be some relative thing in common for all those strings. Ahhh yes, difference in ascii values
        ## 2. Store ascii value pairs in hashmap and group together.
        ## 3. If the diff in ascii become -ve then add 26
        ## Watchout : case : acz (2, 23), dfc (2, -3) ==> (2, -3+26 = 23) => can be clubbed together.
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        groups = collections.defaultdict(list)
        for s in strings:
            pattern = ()
            for i in range(1,len(s)):
                pattern = pattern + ((ord(s[i]) - ord(s[i-1]) + 26 ) % 26,)
            groups[ pattern ].append(s)
        return groups.values()
-----------------------------------------------------------

from collections import defaultdict

class Solution:
    def findKey(self, s):
        if len(s) == 0:
            return -1
        elif len(s) == 1:
            return 1
        
        k = [0] * (len(s)-1)
        
        # Looping through array and finding ascii value diff of (curr_elem - prev_elem) for each, considering modulo(%) 26
        for i in range(1,len(s)):
            k[i-1] = (ord(s[i])-ord(s[i-1]))%26
        
		# for string s = 'acd', k array would look like [2, 1]
		
        # Converting to tuple so that it can be hashed to use as a key of dict
        return tuple(k)
    
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        
        for s in strings:
            # Shifted string is part of the same group if the diff of ascii value between chars of the string is same
            # Eg, 
            # 1. s1 = 'acd', s2 = 'mop'
            #    here, 
            #       for s1, 
            #               ascii_val_of('c') - ascii_val_od('a') is 2
            #               ascii_val_of('d') - ascii_val_od('c') is 1
            #       for s2, 
            #               ascii_val_of('o') - ascii_val_od('m') is 2
            #               ascii_val_of('p') - ascii_val_od('o') is 1
            #    so both s1 and s2 are part of the same group
            # 2. s1 = 'ae', s2 = 'bd'
            #    here, 
            #       for s1, 
            #               ascii_val_of('e') - ascii_val_od('a') is 4
            #       for s2, 
            #               ascii_val_of('d') - ascii_val_od('b') is 2
            #    so s1 and s2 are not part of the same group
            #     
            # Now we can find key using the same approach; check findKey() for understanding how the key is generated
            key = self.findKey(s)
            
            # putting string in the dictionary of the same group
            d[key].append(s)
            
        res = []
        for _, v in d.items():
            res.append(v)
            
        return res
      
----------------------------------------------------------
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {}
        for i in strings:
            hs = self.strHash(i)
            if hs not in dictionary.keys():
                dictionary[hs] = [str(i)]
            else:
                self.insertStr(dictionary[hs],str(i))
        return [dictionary[key] for key in dictionary.keys()]
    
    def strHash(self,astring):
        hslist = [(ord(i)-ord(astring[0])) % 26 for i in astring]
        return tuple(hslist)
    
    def insertStr(self, alist, astring):
        i = 0
        while i < len(alist) and ord(astring[0]) > ord(alist[i][0]):
            i += 1
        if i == len(alist):
            alist.append(astring)
        else:
            alist[:] = alist[0:i] + [astring] + alist[i:]
-----------------------------------------------------------------------------------
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        myDict=defaultdict(list)
        totalDistance=()
        
        for s in strings:
            for l1,l2 in zip(s,s[1:]):
                distance= (26+ord(l1)-ord(l2)) %26  #distance between letter1 and letter22
                totalDistance+=(distance,) #we add distance to the the tuple
            myDict[totalDistance].append(s)
            totalDistance=() #restart totalDistance fo
        return myDict.values()
----------------------------------------

Algorithm:

We are recognizing the pattern of the strings and similar pattern are going to same list.
So, we can group them by length which would be one way, but, then ab and ba would go to same list and that would be wrong as the patterns are different.
Here, similar pattern means that distance between the charachters is same.
So, we know that the similar patterns will have the same distance so we can take the difference between the consecutive letters of a word and generate a list of that.
So, if that list is same for different then we can say that they have similar pattern.
example: abc will generate [1,1] and xyz will also generate [1,1] but this logic has a loophole. We are not given a testcase explicitely that after z in a pattern we have to take a as its next sequence.
So, the sequences za will form a list of [25] and bc which is its next sequence will have a [-1] as the list and hence will be registered as different sequence. So for this we can do that is the difference between consecutive digits is < 0 then we add 26 to it so that it loops back to start.
Now that we have understood the algorithm we still face a difficulty as we cannot hash, list to dictionary but we can hash tuple to python dictionary. (Note: Even I came to know we can do this yesterday so don't worry. You came to know about this today 😀😄)
So, we use tuple for that. So, first we run the loop and add the difference between consecutive letters in a list and then we convert that list to tuple and add that tuple as key in dictionary.
So, now we take the input list and generate the tuple using a function. We add that tuple as the key in dictionary and the elements similar to that tuple in a list and finally give the output as asked.
Shameless-Self-Promotion: My other leetcode solutions to various questions can be found here

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        output = defaultdict(list)
        
        def strToTuple(word):
            
            if len(word) > 1:
                lst = []
                for x in range(len(word)-1):
                    # if ord(word[x]) == 122:
                    diff = ord(word[x]) - ord(word[x+1])
                    
                    if diff < 0:
                        diff = diff + 26
                        
                    lst.append(diff)
                
                return tuple(lst)
            else:
                return 1
        
        for word in strings:
            output[strToTuple(word)].append(word)
        
        return [output[x] for x in output]
Time: O(N * M)
Space: O(N)

where N is the length of the input list M is the length of longest word.

      
            
      
