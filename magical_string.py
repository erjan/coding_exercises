'''
A magical string s consists of only '1' and '2' and obeys the following rules:

The string s is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string s itself.
The first few elements of s is s = "1221121221221121122……". If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2 ......". You can see that the occurrence sequence is s itself.

Given an integer n, return the number of 1's in the first n number in the magical string s.

 
 '''

def magicalString(self, n: int) -> int:
	s = ["1", "2", "2"]
	for i in range(2, n):
		p = s[-1] == "2"
		if(s[-1] == '2'):
			s += ["1"] * int(s[i])
		else:
			s += ["2"] * int(s[i])
		if(len(s) > n): break
	return s[:n].count('1')

--------------------------------------------------------
class Solution:
    def magicalString(self, n: int) -> int:
        ref = "122112"
        actual = ""
        start = 0
        one = True
        
        while(len(ref) < n):
            for i in range(start, len(ref)):
                if(one):
                    actual += int(ref[i]) * "1"
                    one = False
                else:
                    actual += int(ref[i]) * "2"
                    one = True
                    
            if(len(actual) > len(ref)):
                start = len(ref)
                ref = actual
        
        return ref[:n].count("1")
