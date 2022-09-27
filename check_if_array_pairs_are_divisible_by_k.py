'''
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.
'''

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        from collections import defaultdict
        visited=defaultdict(lambda :0)
        pairs=0

        for num in arr:

            mod=num%k

            if visited[(-1*(k+mod)) ] >0:
                pairs+=1
                visited[(-1*(k+mod)) ]-=1

            elif visited[(k-mod)]>0:
                pairs+=1
                visited[(k-mod)]-=1

            elif visited[(-1*mod )]>0:
                pairs+=1
                visited[(-1*mod )]-=1

            else: visited[mod]+=1

        return pairs==len(arr)//2
