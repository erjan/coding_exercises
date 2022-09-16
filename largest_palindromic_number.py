'''
You are given a string num consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Notes:

You do not need to use all the digits of num, but you must use at least one digit.
The digits can be reordered.
 
 '''

Explanation
Count the frequency of all digits in num
Check how many pair of 9 that we have:
If we have one pair of 9, we can make 9XXXXXX9, res = '99' now.
If we have two pairs of 9, we can make 99XXXX99, res = '9' now.
Continue check pairs for 8,7,6,5,4,3,2,1,0
Strip the leading 0 in res
Find the maximum digit left that can be used for the middle digit of palindromic number.
final result is res + mid + reversed(res)
For special input like 00, we need to return 0.

    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        res = ''.join(count[i] // 2 * i for i in '9876543210').lstrip('0')
        mid = max(count[i] % 2 * i for i in count)
        return (res + mid + res[::-1]) or '0'
      
------------------------------------------------------------------------
class Solution:
    def largestPalindromic(self, num: str) -> str:
        c = Counter(num)
        if len(c)==1 and c['0']>=1:
            return "0"
        m = -1   #storing the mid of the number
        res1 = ''
        res2 = ''
        for i in range(9,-1,-1):
            while c[str(i)]:
                if not res1 and i==0:   #to avoid adding 0 at first
                    break 
                if c[str(i)]>=2:

                    res1 += str(i)
                    res2 = str(i) + res2
                    c[str(i)]-=2
                if c[str(i)] == 1:
                    m = max(m,i)  #updating medium to max
                    c[str(i)]-=1
                if c[str(i)]==0:
                    del c[str(i)]
        return res1+res2 if m==-1 else res1 + str(m) + res2
