'''
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]

'''


Some observation to the sequence:

n == 1: [0, 1, 8]

n == 2: [11, 88, 69, 96]

How about n == 3?
=> it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 2

n == 4?
=> it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 2

n == 5?
=> it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 4

the same, for n == 6, it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 4

def findStrobogrammatic(self, n):
    evenMidCandidate = ["11","69","88","96", "00"]
    oddMidCandidate = ["0", "1", "8"]
    if n == 1:
        return oddMidCandidate
    if n == 2:
        return evenMidCandidate[:-1]
    if n % 2:
        pre, midCandidate = self.findStrobogrammatic(n-1), oddMidCandidate
    else: 
        pre, midCandidate = self.findStrobogrammatic(n-2), evenMidCandidate
    premid = (n-1)/2
    return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]
  
-------------------------------------------------------

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # Special case: n = 1
        if n == 1:
            return ['0', '1', '8']
        
        return [num for num in self.findStrobogrammatic_helper(n) if num[0] != '0' and num[-1] != '0']
        
        
    def findStrobogrammatic_helper(self, n):
        # Base cases
        if n == 1:
            return ['0', '1', '8']
        if n == 2:
            return ['00', '11', '88', '69', '96']
        
        results = []
        for base in self.findStrobogrammatic_helper(n-2):
            results.append('6' + base + '9')
            results.append('9' + base + '6')
            results.append('1' + base + '1')
            results.append('8' + base + '8')
            results.append('0' + base + '0')
        return results
      
----------------------------------------------------------

A bit verbose but hopefully easier to understand. We start from the middle and expand out.

Time complexity O(n). We iterate n//2 times in for _ in range(n//2). Within this, we iterate for num in output at most 5 times, since output has at most 5 numbers.

Space complexity O(1). temp uses constant space of at most 5.

def findStrobogrammatic(self, n):
	output = [''] if n%2 == 0 else ['0', '1', '8']
	
	for _ in range(n//2):
		temp = []
		for num in output:
			temp.append('1' + num + '1')
			temp.append('8' + num + '8')
			temp.append('6' + num + '9')
			temp.append('9' + num + '6')
			if len(num) < n-2:
				temp.append('0' + num + '0')
		output = temp

	return output

---------------------------------------------------------------------

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        center = ['0','1','8']                      # center in case of odd length only
        ends = ['11','88','69','96']                # 0 cannot be first character
        middle = ['00','11','88','69','96']         # elsewhere in the string but middle and ends
        # initialize the result list
        if n%2==0:
            curr=['']                               # empty string is strobogrammatic
        else:
            curr=center                             # only odd length has center character
        # We use a growing technique, appending two characters to both ends of current string
        # We use prev to store results of current iteration which will be used to run the next iteration
        prev = None                                 
        m = n//2                                    # since we attach 2 characters at a time
        while m>0:
            prev = curr                             # store results of previous iteration
            curr = []                               # empty curr to append all new strings
            arr = ends if m==1 else middle          # to avoid attaching a '0' to the front
            for itm in arr:
                for wrd in prev:
                    curr.append(itm[0]+wrd+itm[1])
            m-=1
        return curr
--------------------------------------------------------------------------

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        num2num = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        res = []
        if n % 2 == 0:
            self.dfs(res, '', n, num2num)
        else:
            for num in {'0', '1', '8'}:
                self.dfs(res, num, n, num2num)
        
        return res
    
    def dfs(self, res, s, n, num2num):
        if len(s) == n:
            res.append(s)
            return 
        
        for num1, num2 in num2num.items():
            if len(s) == n - 2 and num1 == '0':
                continue
            
            self.dfs(res, num1 + s + num2, n, num2num)
--------------------------------------------------------------------------------------            
            
      
