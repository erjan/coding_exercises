'''
You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

'''


class Solution:
    def largestInteger(self, num: int) -> int:
        
        s = str(num)
        
        s = list(s)
        s = [int(i) for i in s]
        
        evens = list()
        odds = list()
        
        for i in range(len(s)):
            
            if s[i] %2 == 0:
                evens.append(s[i])
            else:
                odds.append(s[i])
        
        evens.sort(reverse=True)
        odds.sort(reverse=True)
        
        res = ''
        for i in range(len(s)):
            if s[i] %2 == 0:
                res += str(evens[0])
                evens.pop(0)
            else:
                res+= str(odds[0])
                odds.pop(0)
        return int(res)
            
        
        
----------------------------------------
class Solution:
    def largestInteger(self, num: int):
        n = len(str(num))
        arr = [int(i) for i in str(num)]
        odd, even = [], []
        for i in arr:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        odd.sort()
        even.sort()
        res = 0
        for i in range(n):
            if arr[i] % 2 == 0:
                res = res*10 + even.pop()
            else:
                res = res*10 + odd.pop()
        return res
------------------------------------
#priority queue solution

from queue import PriorityQueue

class Solution:
    def largestInteger(self, num: int) -> int:
        arr = []
        arr.extend(str(num))
        arr = list(map(int, arr))
        pq1 = PriorityQueue()
        pq2 = PriorityQueue()
        
        for i in range(len(arr)):
            if(arr[i] % 2 == 0):
				# Converting min heap to max heap
                pq1.put((-1*arr[i], i))
            else:
                pq2.put((-1*arr[i], i))
                
        ans = []
        
        for i in range(len(arr)):
            
            if(arr[i] % 2 == 0):
                index = pq1.get()[1]
                ans.append(arr[index])
                
            else:
                index = pq2.get()[1]
                ans.append(arr[index])
                
                
        return "".join(map(str, ans))
        
