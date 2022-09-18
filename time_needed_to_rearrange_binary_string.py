'''
You are given a binary string s. In one second, all occurrences of "01" are simultaneously replaced with "10". This process repeats until no occurrences of "01" exist.

Return the number of seconds needed to complete this process.
'''

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        
        seconds = 0

        res = s.count('01')

        while s.count('01') != 0:
            seconds += 1

            s = s.replace('01', '10')

        print(s)
        print(seconds)
        return seconds
      
-----------------------------------------------------------------
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:

        ans = 0

        while '01' in s:
            ans += 1
            s = s.replace('01', '10')
            
        return ans
---------------------------------------------------------------------------------
class Solution:
	def secondsToRemoveOccurrences(self, s: str) -> int:
		count = 0
		temp = ""
		ones = s.count("1") # get the count of 1
		for _ in range(ones):
			"""
			make a string with total number of 1
			"""
			temp += "1"

		while s[:ones] != temp:
			"""
			loop through index 0 to count of 1 while the string is not equal to temp string
			"""

			left, right = 0, 1
			while right < len(s):
				"""
				Compare the two index from left to right if
				they both are equal to "01"
				if so then replace them
				and count the number of occurrence
				"""
				if s[left : left + 1] + s[right : right + 1] == "01":
					s = s.replace(s[left : left + 1] + s[right : right + 1], "10")
					count += 1
				left += 1
				right += 1
		return count
------------------------------------------------------------------------------------------------  

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count=0
        def recurbinary(s):
            nonlocal count
            if "01" in s:
                count=count+1
                s=s.replace("01","10")
                recurbinary(s)
            return 
        recurbinary(s)
        return count

--------------------------------------------
DP

class Solution {
public:
    int secondsToRemoveOccurrences(string s) {
        int zeros = 0, seconds = 0;
        for (int i = 0; i < s.size(); ++i) {
            zeros += s[i] == '0' ? 1 : 0;
            if (s[i] == '1' && zeros > 0)
                seconds = max(seconds + 1, zeros);
        }
        return seconds; 
    }
};
