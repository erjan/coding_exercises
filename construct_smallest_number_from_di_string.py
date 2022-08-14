'''
You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.
'''


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
		
		#smallest possible string
        smallest = [f'{i+1}' for i in range(n+1)]
        
		#inplace reversal
        def reverse(arr,start,end):
            if start>=end:
                return
            
            arr[start],arr[end] = arr[end],arr[start]
            reverse(arr,start+1,end-1)
        
        i = 0
        while i<n:
		#starting of the sequence of Ds
            if pattern[i]=='D':
                j = i #ending index of sequence of Ds
                while j+1<n and pattern[j+1]=='D':
                    j+=1
					
				#reverse the sequence
                reverse(smallest,i,j+1)
				
				#move front
                i = j+1
            else:
                i+=1
                
        return "".join(smallest)
