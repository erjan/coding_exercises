'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.


Maintain 2 pointers lo and hi set to 0 and n-1 respectively.
Sort the array people.
Now traverse till lo <= hi.
If people[lo] + people[hi] <= target. That means they can form a pair and can sit in the same boat.
If not then the people[hi] that is the person with the higher weight is the problem and must be given his own boat as we observed above.
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo = 0
        hi = len(people)-1
        boats = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
                hi -= 1
            else:
                hi -= 1
            boats += 1
        return boats
      
-----------------------------------------------------------------------------------------------------

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=0
        i, j =0, len(people)-1
        while i <= j :
            if people[j]==limit or people[i]+people[j]>limit:
                j-=1
                count+=1
            else:
                i+=1
                j-=1
                count+=1
        return count
