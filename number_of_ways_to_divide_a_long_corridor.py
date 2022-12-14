'''
Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.

 
 '''

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        l=len(corridor)
        count=0
        last=-1
        ans=1
        for i in range(l):
            if corridor[i]=='S':
                count+=1
                if count%2==0:
                    last=i
                elif count%2==1 and last!=-1:
                    ans*=(i-last)
        if count%2!=0 or count==0:
            return 0
        return ans%1000000007

------------------------------------------------------------------
class Solution:
    def numberOfWays(self, corridor: str) -> int:

        # go through the corridor and count seats
        # after that check whether there are plants
        # and we have several places to divide

        # go through the chairs and count
        chairs = 0
        positions = 1
        plants = 1
        for idx, element in enumerate(corridor):

            # check if we reached two chairs
            if chairs > 0 and chairs % 2 == 0:

                # check if current element is plant
                if element == 'S':
                    positions *= plants
                    plants = 1
                
                elif element == 'P':
                    plants += 1

            # count the chairs
            if element == 'S':
                chairs += 1
        return (positions % 1_000_000_007) if chairs > 0 and chairs % 2 == 0 else 0
      
