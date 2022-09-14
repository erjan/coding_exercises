'''
Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.
'''
-----------------------------------------------------------------------------------------------------
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans, sumNum, cnt = 1, 1, 2
        while sumNum < n:
            if sumNum % cnt == n % cnt: ans += 1
            sumNum += cnt
            cnt += 1
        return ans
      
      
The point of this problem is, it should be divided into consecutive numbers.

Let's think about dividing the number 15.

If we want to break 15 down to three consecutive numbers, it should be like m / m + 1 / m + 2(or m - 1 / m / m + 1, or m - 2 / m - 1 / m), which is 4 / 5 / 6 and m is 4 in this case.

If it's divided into five chunks, it should be like m / m + 1 /m + 2 / m + 3 / m + 4, which will be 1 / 2 / 3 / 4 / 5 and m is 1.

So we can say the number n can be expressed as k*m + Sum{0~(k-1)} if the number n is split into k pieces.

Now, all we have to do is to see if the result of Sum{0~(k-1)} % k is equal to n % k because if they have the same remainders, it means we can successfully split n into k consecutive numbers.

In my code, sumNum is the result of Sum{0~(k-1)} and cnt is the k number and also the next number to be added to sumNum at the same time. Running though the loop, the code checks the value of remainders and keeps adding numbers to sumNum and cnt.

The loop ends when sumNum is equal or bigger than the number n because the sum of remainders shouldn't be bigger than n.
