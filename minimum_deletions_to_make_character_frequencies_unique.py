'''
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

First we find the count of each and every element making use of a hashmap
We then define a variable res = 0 to store the count
We also make a set (used) to check if we have all unique elements.
We then make use of a while loop to check the condition
We make use of a while loop instead of making use of if condition because we may have to do more than 1 deletion operation.
If the value is greater than 0 and if it already exists in the set (used) then increment the result and decrement the value by 1.
Return the result.


'''

class Solution:
    def minDeletions(self, s: str) -> int:
        
        S = collections.Counter(s)
    
        count= 0

        unique = set()

        for char, freq in S.items():
            while freq >0 and freq in unique:
                freq-=1
                count+=1

            unique.add(freq)

        return count
