'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
      
------------------------------------------------------------
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
		# Store all levels as arr inside a larger levels arr
        levels = []
        for n in range(numRows):
            levels.append([])

        # Iterate through letters of the string
		# For each letter, append it to the level that corresponds to the level variable below
		# Add step to level to increase/decrease level
        level = 0
        step = 1
        
        for letter in s:
            levels[level].append(letter)
            level += step
            
			# Step turns negative when we reach the last level
			# Step turns positive when we reach the top level
            if level == 0 or level == numRows-1:
                step *= -1
        
		# Convert the list of letter into strings
        for level, string in enumerate(levels):
            levels[level] = ''.join(string)
           
        return ''.join(levels)
