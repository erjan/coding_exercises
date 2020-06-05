#There are 2N people a company is planning to interview. 
#The cost of flying the i-th person to city A is costs[i][0], and 
#the cost of flying the i-th person to city B is costs[i][1].

#Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        costs = sorted(costs, key=lambda x: abs(x[0]-x[1]), reverse=True)# this is key - to observe that we need to sort by diff in costs.
        N = len(costs)//2
 
        countA = N
        countB = N
        
        for citya, cityb in costs:
            if countA > 0 and countB > 0:
                if citya < cityb:
                    countA-=1
                    res+= citya
                else:
                    countB-=1
                    res+=cityb
            elif countA == 0:
                res+=cityb
            else:
                res+=citya
        return res
            
