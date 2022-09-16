'''
You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.
'''

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        odd, even = defaultdict(int), defaultdict(int)
        for i in range(n):
            if i % 2 == 0:
                even[nums[i]] += 1
            else:
                odd[nums[i]] += 1
        topEven, secondEven = (None, 0), (None, 0)
        for num in even:
            if even[num] > topEven[1]:
                topEven, secondEven = (num, even[num]), topEven
            elif even[num] > secondEven[1]:
                secondEven = (num, even[num])
        topOdd, secondOdd = (None, 0), (None, 0)
        for num in odd:
            if odd[num] > topOdd[1]:
                topOdd, secondOdd = (num, odd[num]), topOdd
            elif odd[num] > secondOdd[1]:
                secondOdd = (num, odd[num])
        if topOdd[0] != topEven[0]:
            return n - topOdd[1] - topEven[1]
        else:
            return n - max(secondOdd[1] + topEven[1], secondEven[1] + topOdd[1])
          
-----------------------------------------------------------------------------------

class Solution:  # works
    def minimumOperations(self, nums: List[int]) -> int:
        end = len(nums)
        def freq(start):
            counter = dict()
            for i in range(start, end, 2):
                if nums[i] not in counter:
                    counter[nums[i]] = 1
                else:
                    counter[nums[i]] += 1
            return counter
        odd, even = freq(0), freq(1)
        odd_sum, even_sum = sum(odd.values()), sum(even.values())
        odd = [(k, v) for k, v in odd.items()]
        even = [(k, v) for k, v in even.items()]
        odd = sorted(odd, key=lambda i:i[1], reverse=True)
        even = sorted(even, key=lambda i: i[1], reverse=True)
        for i in odd:
            for j in even:
                if i[0] != j[0]:
                    return odd_sum - i[1] + even_sum - j[1]
        return min(odd_sum, even_sum)
      
-----------------------------------------------------------------

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even, odd = {}, {}
        maxEvenFreq, maxOddFreq = [None, 0], [None, 0]
        secondMaxEvenFreq, secondMaxOddFreq = [None, 0], [None, 0]
        
        for i, num in enumerate(nums):
            if i & 1:
                if num in odd:
                    odd[num] += 1
                else:
                    odd[num] = 1
            else:
                if num in even:
                    even[num] += 1
                else:
                    even[num] = 1

        for num in odd:
            if odd[num] > maxOddFreq[1]:
                maxOddFreq, secondMaxOddFreq = [num, odd[num]], maxOddFreq
            elif odd[num] > secondMaxOddFreq[1]:
                secondMaxOddFreq = [num, odd[num]]
        
        for num in even:
            if even[num] > maxEvenFreq[1]:
                maxEvenFreq, secondMaxEvenFreq = [num, even[num]], maxEvenFreq
            elif even[num] > secondMaxEvenFreq[1]:
                secondMaxEvenFreq = [num, even[num]]
        
        if maxEvenFreq[0] != maxOddFreq[0]:
            return len(nums) - (maxEvenFreq[1] + maxOddFreq[1])
        else:
            return len(nums) - max(maxEvenFreq[1] + secondMaxOddFreq[1],  maxOddFreq[1] + secondMaxEvenFreq[1])
