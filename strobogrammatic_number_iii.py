Given two strings low and high that represent two integers 
low and high where low <= high, return the number of strobogrammatic numbers in the range [low, high].

A strobogrammatic number is a number that looks the same when 
rotated 180 degrees (looked at upside down).



class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        l, u = len(low), len(high)
        ans = []
        for n in range(l, u+1): 
            self.dfs(0, n-1, ["" for _ in range(n)], ans, n, int(low), int(high))
        return len(ans)
        
    def dfs(self, currentIndex, endIndex, ansList, new_ans, n, low_limit, upper_limit):
        if currentIndex > endIndex:
            ans = ''.join(ansList[:])
            if int(ans) >= low_limit and int(ans) <= upper_limit:
                new_ans.append(ans)
            return 
        if currentIndex == endIndex:
            for letter in ['0', '1', '8']:
                ansList[currentIndex] = letter
                ans = ''.join(ansList[:])
                if int(ans) >= low_limit and int(ans) <= upper_limit:
                    new_ans.append(ans)
            return 
        
        
        for letter in ['0', '1', '6', '8', '9']:
            if currentIndex != 0:
                if letter == '0':
                    ansList[currentIndex] = '0'
                    ansList[endIndex] = '0'
                    self.dfs(currentIndex + 1, endIndex - 1, ansList, new_ans, n, low_limit, upper_limit)
                elif letter == '1':
                    ansList[currentIndex] = '1'
                    ansList[endIndex] = '1'
                    self.dfs(currentIndex + 1, endIndex - 1, ansList, new_ans, n, low_limit,upper_limit)
                elif letter == '8':
                    ansList[currentIndex] = '8'
                    ansList[endIndex] = '8'
                    self.dfs(currentIndex + 1, endIndex - 1, ansList, new_ans, n, low_limit,upper_limit)
                elif letter == '6':
                    ansList[currentIndex] = '6'
                    ansList[endIndex] = '9'
                    self.dfs(currentIndex + 1, endIndex - 1, ansList, new_ans, n, low_limit,upper_limit)
                else:
                    ansList[currentIndex] = '9'
                    ansList[endIndex] = '6'
                    self.dfs(currentIndex + 1, endIndex - 1, ansList, new_ans, n, low_limit,upper_limit)
            
            else:
                if letter == '1':
                    ansList[currentIndex] = '1'
                    ansList[endIndex] = '1'
                    self.dfs(currentIndex + 1, endIndex - 1, ansList, new_ans, n,low_limit, upper_limit)
                elif letter == '8':
                    ansList[currentIndex] = '8'
                    ansList[endIndex] = '8'
                    self.dfs(currentIndex + 1, endIndex - 1, ansList, new_ans, n, low_limit,upper_limit)
                elif letter == '6':
                    ansList[currentIndex] = '6'
                    ansList[endIndex] = '9'
                    self.dfs(currentIndex + 1, endIndex - 1, ansList, new_ans, n, low_limit,upper_limit)
                elif letter == '9':
                    ansList[currentIndex] = '9'
                    ansList[endIndex] = '6'
                    self.dfs(currentIndex + 1, endIndex - 1, ansList, new_ans, n, low_limit,upper_limit)
                else: 
                    continue 
                    
-----------------------------------------------------------------------           


O((5 ^ (n/2)) - where N is the character length of high
Space: recursion stack O((5 ^ (n/2)) - where N is the character length of high
Algorithm: use result from LC#247 and construct all the strobogrammatic numbers in length low to high, then count the ones which are within the specified range.


def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        all_strobo = []
        for length in range(len(low), len(high) + 1):
            all_strobo += self.strobo(length)
        res = 0
        for num in all_strobo:
            if int(low) <= int(num) <= int(high):
                res += 1
        return res
        
    def strobo(self, n):
        self.mapping = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
        self.res = []
        if n % 2:
            for i in ["0", "8", "1"]:
                self.dfs(str(i), n - 1)
        else:
            self.dfs("", n)
        return self.res
        
    def dfs(self, num, n):
        if n == 0:
            self.res.append(num)
            return
            
        for number in self.mapping:
            if n == 2 and number != "0":
                self.dfs(number + num + self.mapping[number], n - 2)
            elif n > 2:
                self.dfs(number + num + self.mapping[number], n - 2)            
                         
                         
-------------------------------------------------------------------------------
                         class Solution:
# @param {string} low
# @param {string} high
# @return {integer}
def strobogrammaticInRange(self, low, high):
    a=self.below(high)
    b=self.below(low,include=False)
    return a-b if a>b else 0

'''
get how many strobogrammatic numbers less than n
'''
def below(self,n,include=True):
    res=0
    for i in range(1,len(n)):
        res+=self.number(i)
    l=self.strobogrammatic(len(n))
    '''
    filter num larger than n and start with 0
    '''
    if include:
        l=[num for num in l if (len(num)==1 or num[0]!='0') and num<=n]
    else:
        l=[num for num in l if (len(num)==1 or num[0]!='0') and num<n]
    return res+len(l)

'''
get strobogrammatic numbers with length l
number start with 0 would be included
'''
def strobogrammatic(self,l):
    res=[]
    if l==1:
        return ['0','1','8']
    if l==2:
        return ['00','11','69','96','88']
    for s in self.strobogrammatic(l-2):
        res.append('0'+s+'0')
        res.append('1'+s+'1')
        res.append('6'+s+'9')
        res.append('8'+s+'8')
        res.append('9'+s+'6')
    return res

'''
get number of strobogrammatic numbers of length l
'''
def number(self,l):
    if l==0:
        return 0
    '''
    If l is an even number, the first digit has four choices (1,6,8,9). digits 
    at other position have five choices(0,1,6,8,9)
    '''
    if l%2==0:
        return 4*(5**(l/2-1))
    '''
    If l is an odd number, the first digit has four choices (1,6,8,9) and digit 
    at the middle has 3 choices (0,1,8),other digits have 5 choices.
    digit at other position could be 0,1,6,8,9
    '''
    elif l==1:
        return 3
    else:
        return 3*(5**(l/2-1))*4
