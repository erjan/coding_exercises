'''
You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.
'''




'''
Intuition
A mechanic can repair n cars in r * n * n minutes. So in mid minutes a mechanic can repair n cars where, n = sqrt(mid / r)
Let's assume that the correct answer is mid minutes, we can find the number of cars each mechanic can repair in mid minutes, then find the find the total number of cars fixed. If total number of cars fixed is greater than or equal to the cars we have to repair, mid minutes is a valid answer, else we have to increase mid. We can not linearly calculate total cars fixed for each mid in (0 to 10^14), we must use binary search to lower the time complexity.

Approach
Total cars repaired by all workers in mid minutes must be greater than or equal to total cars that have to be repaired
Binary search over the range 0 to 10^14 to find what is the minimum time required to repair all cars
We use high as 10^14 because max(rank) = 100 and max(cars) = 10^6 so, r * n * n = 100 * 10^6 * 10^6 = 10^14
'''

def repairCars(self, A: List[int], cars: int) -> int:
    return bisect_left(range(10**14), cars, key=lambda x: sum(int(sqrt(x / a)) for a in A))
  
------------------------------------------------------------------------------------------------
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        lo,hi = 0,100*cars*cars
        def repair(time):
            n = cars
            for r in ranks:
                n -= floor(sqrt(time/r))
                if n<=0:
                    break
            return n<=0
        while lo<=hi:
            m = (lo+hi)//2
            if repair(m):
                ans = m
                hi = m-1
            else:
                lo = m+1
        return ans
      
---------------------------------------------------------------------------
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        count=Counter(ranks)
        left=1
        right=min(count)*cars*cars
        while left<right:
            mid=(left+right)//2
            if sum(isqrt(mid//a)*count[a] for a in count)<cars:
                left=mid+1

            else:
                right=mid

        return left            
      
------------------------------------------------------------------------------------------
The worst case is that the max rank repairs all cars, and the corresponding time cost is the higher bound of our search space;
Set the lower bound as 0;
Binary search the minimum time need to repair all cars.

    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def canFinish(time: int) -> bool:
            finish = 0
            for r in ranks:
                finish += floor(math.sqrt(time / r))
                if finish >= cars:
                    return True
            return False

        lo, hi = 0, max(ranks) * cars * cars
        while lo < hi:
            time = lo + (hi - lo) // 2
            if canFinish(time):
                hi = time
            else:
                lo = time + 1
        return lo
