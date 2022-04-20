'''
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.
'''

Key ideas:

ans is the array that will store the answer
Step 1: For every update with startIdx, endIdx, and incrementValue:
ans[startIdx] += incrementValue
ans[endIdx + 1] -= incrementValue (if endIdx + 1 is not out of range. If it is out of range, we don't do anything)
Step 2: At the end, we iterate the array from index 1 (0-based indexing), and set:
ans[i] += ans[i-1]. This is basically prefix-sum
Why does this approach work? Let's go over an example. Supposed we have the input:

length = 5, updates = [[1,3,2]]

Notice how we have only 1 update to process. Let's perform Steps 1 and 2 from the key idea section above.

Step 1: The value of ans will be:

[0, 2, 0, 0, -2] (we updated index 1 and 4)

Step 2: The value of ans will be:

[0, 2, 2, 2, 0]

Notice how the 4-th index gets back to 0. This is because as we cascade the value index 0 to the end of the array, if we don't have:

ans[endIdx + 1] -= incrementValue 
Our array will be come
[0, 2, 2, 2, 2]. The bold number is of incorrect value since we only want to update from indices 1 to 3. Therefore, we need to account for the indices that we don't want to add incrementValue to when we perform step 2. How do we do that? By initially setting those indices to the opposite of incrementValue so when we perform the prefix sum step (step 2), the values at those indices will be 0.

Here is the complete code:

ans = [0] * length
for start, end, value in updates:
    ans[start] += value
    end += 1
    if end < len(ans):
        ans[end] -= value

for i in range(1, len(ans)):
    ans[i] += ans[i-1]

return ans
--------------------------------------
                                   
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ## RC ##
        ## APPROACH : GREEDY ##
        ## LOGIC ##
        ## 1. Instead of incrementing all the elements of the array
        ## 2. We add update value at the start of the updateStart, and decrement at the index after the updateEnd.
        ## 3. so we need to initialize answer array with length + 1
        ## 4. we do a running sum and replace it in ans[i], we get correct values
        
        ## Example : length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]] ##
        ## STACK TRACE ##
        # [0, 2, 0, 0, -2, 0]
        # [0, 2, 3, 0, -2, -3]
        # [-2, 2, 3, 2, -2, -3]
        # [-2, 0, 3, 5, 3, 0] ==> final result
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        ans = [0] * (length + 1)
        for update in updates:
            ans[update[0]] += update[2]
            ans[update[1]+1] -= update[2]
            # print(ans)
            
        print([ i+1 for i in range(100) ])
        print(ans)
        sum = 0
        for i,num in enumerate(ans):
            sum += num
            ans[i] = sum
        print(ans)
        return ans[:-1]
                                   
----------------------------------------------------
                                   
                                   class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0 for _ in range(length)]
        carries =  [0 for _ in range(length)]  
        for upd in updates:
            result[upd[0]] += upd[2]
            
            carries[upd[0]] += upd[2]
            carries[upd[1]] += (-1*upd[2])
            
        carry = 0    
        for i in range(len(result)):
            result[i] += carry
            carry += carries[i]
        return result        
                                   
----------------------------------
                                   
                                   We will do a cumulative sum at all start points till end of array by storing the increment value at start points. This will not affect points before the start but it will affect all those after end. Hence, we decrement the same value at point end + 1. O(N + K) time.

def getModifiedArray(self, length, updates):
	arr = [0 for _ in range(length+1)]
	for start, end, inc in updates:
		arr[start] += inc
		arr[end+1] -= inc
	for i in range(1, length+1):
		arr[i] = arr[i] + arr[i-1]
	return arr[:-1]
                                   
-----------------------------------------
                                   
                                   First of all, we can use the brute-force way to construct the result list. That is for each update, we iterate from the start index to the end index of the result list to update the elements in the list. For each update we can use O(k) time complexity, where k is the length. And we can update for n times, where n is the lenght of updates. Therefore, the brute-force way will take time complexity of O(k * n), and no extra space needed other than the return list itself.

Then we can think if it is a smarter solution, do we have to iterate through the return list for every update, and can we do it all once? Yes, of course! We can observe a pattern. That is for each update, we raise a surplus at the start, and keep it going on till the end of the update. Then we can only keep one variable, and the update positions (start and end). Therefore, we can have a list storing the indices and how much we want to update the variable for every possible update.

For the result, we can simply update the storing list to save space, since the update information before is no longer useful. Then for the time complexity, we have O(n + k), since we iterate through the return list once and the updates list once as well. For the space, again, we take no extra space other than the return list itself.

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        # set up the storage space
        surplus = [0 for _ in range(length)]
        
        # iterate through the updates to construct the surplus needed for each position
        for start, end, inc in updates:
            surplus[start] += inc
            if end+1 < length:
                surplus[end+1] -= inc
        
        # iterate through the storage space to update the culmulative surplus
        # then calculate the final result 
        culSurplus = 0
        for i in range(length):
            culSurplus += surplus[i]
            surplus[i] = culSurplus
        
        return surplus
                                   
--------------------------------------------------------------------------------------                                   
                                   
