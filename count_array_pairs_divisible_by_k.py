'''
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums[i] * nums[j] is divisible by k.
'''

Explanation
Count all elements greatest common divisor with k.
For each pair (a, b) of divisors, check if a * b % k == 0


def coutPairs(self, A, k):
        cnt = Counter(math.gcd(a, k) for a in A)
        res = 0
        for a in cnt:
            for b in cnt:
                if a <= b and a * b % k == 0:
                    res += cnt[a] * cnt[b] if a < b else cnt[a] * (cnt[a] - 1) // 2
        return res
      
--------------------------------------------------------------------------------------------------------------------------
class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        N, output = len(nums), 0
        divisors = []
        counter = Counter()
        
        for i in range(1, k + 1):
            if k % i == 0:
                divisors.append(i)
For each number, there is the smallest value to multiply that makes it divisible by 'k'
ex: 6 should be multiplied by at least 2 to be divisible by 4
     4 should be multiplied by at least 1 to be divisible by 4
     3 should be multiplied by at least 4 to be divisible by 4

Divisors collects all the posiibility of those smallest numbers

divisor = [1,2,4]

        for i in range(0, N):
            remainder = k // math.gcd(k, nums[i])
			output += counter[remainder]
remainder calculate how much num[i] should at least be multiplied to be divisible by 'k'
Ex: num[i] = 6 -> reminder = 4 // gcd(4,6) = 2
"counter[remainder]" indicates how many numbers in 'nums' are divisible by remainder(2)

            for divisor in divisors:
                if nums[i] % divisor == 0:
                    counter[divisor] += 1
            
        return output
Then define which group num[i] belongs to
Ex: nums[i] = 6, then nums[i] is divisible by 1, 2
     whick mean if the remainder of nums[n] is 1 or 2 it can pair with '6'
