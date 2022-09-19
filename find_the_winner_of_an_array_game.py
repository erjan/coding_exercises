'''
Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.
'''


def getWinner(self, arr: List[int], k: int) -> int:
		#TLE
        # curr=-1
        # curr_count=0
        # maxi=max(arr)
        # if k>=len(arr):
        #     return maxi
        # while True:
        #     a,b=arr[0],arr[1]
        #     if a>b:
        #         if a==curr:
        #             curr_count+=1
        #         else:
        #             curr=a
        #             curr_count=1
        #         arr[1:]=arr[2:]+[b]
        #     else:
        #         if b==curr:
        #             curr_count+=1
        #         else:
        #             curr=b
        #             curr_count=1
        #         arr[0]=b
        #         arr[1:]=arr[2:]+[a]
        #     if curr_count>=k:
        #         return curr
        #     # print(arr)
        # return -1
		
		#Optimized
        curr=arr[0]
        curr_count=0
        for i in range(1, len(arr)):
            if arr[i]>curr:
                curr=arr[i]
                curr_count=1
            else:
                curr_count+=1
            if curr_count>=k:
                return curr
        return curr
