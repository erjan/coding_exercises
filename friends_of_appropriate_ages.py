'''
There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

Return the total number of friend requests made.
'''

Algorithm
Step 1: construct a dictionary with age as key and number of members in that age group as values. This can be done using Counter in collections module.
Step 2: iterate for every age group (not every person!!) say "me"
Step 3: for every age group check condition take ("age","me") pair and check if the conditions asked are satisfied with

age<= 0.5 * me +7
age>me
3rd condition is always false so we can omit it.
Step 4:
Here we have 2 cases.

case(a): if your age is different from the other age
for example 16,15,15 then 15->16 and 15->16
ie 2*1 which is age_count * me_count
case(b): if your age is same as other age
for example 16,16 then 16<->16 ie 2.
This would be same as number of edges in a graph with n vertices where each edge considered 2 times which is 2*nC2 which would be me_count*(me_count-1)
Python code
from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count=0
		# Step 1
        dicto=Counter(ages)
		# Step 2
        for me in dicto:
            my_age_count=dicto[me]
			# Step 3
            for age in dicto:
                if not (age<= 0.5 * me +7 or age>me):
					# Step 4 case (a)
                    if age!=me :
                        count+=dicto[age]*my_age_count
					# Step 4 case (b)
                    else:
                        count+=int(my_age_count*(my_age_count-1))
        return count
      
--------------------------------------------------------
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()                                   # sort the `ages`
        ans = 0
        n = len(ages)
        for idx, age in enumerate(ages):              # for each age
            lb = age                                  # lower bound
            ub = (age - 7) * 2                        # upper bound
            i = bisect.bisect_left(ages, lb)          # binary search lower bound
            j = bisect.bisect_left(ages, ub)          # binary search upper bound
            if j - i <= 0: continue
            ans += j - i                              # count number of potential friends
            if lb <= age < ub:                        # ignore itself
                ans -= 1
        return ans
-------------------------------------------
class Solution(object):
    def numFriendRequests(self, ages):
        count = [0] * 121                           # counter: count frequency of each age
        for age in ages:
            count[age] += 1
        ans = 0
        for ageA, countA in enumerate(count):       # nested loop, pretty straightforward
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA
        return ans  
      
