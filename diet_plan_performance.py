'''
A dieter consumes calories[i] calories on the i-th day. 

Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they look at T, the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):

If T < lower, they performed poorly on their diet and lose 1 point; 
If T > upper, they performed well on their diet and gain 1 point;
Otherwise, they performed normally and there is no change in points.
Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for calories.length days.

Note that the total points can be negative.
'''


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        
        score  = 0
        first_calories = sum(calories[0:k])
        
        if first_calories > upper:
            score+=1
        if first_calories < lower:
            score-=1
        
        
        for i in range(k, len(calories)):
            first_calories += calories[i] - calories[i -k]
            
            if first_calories > upper:
                score+=1
            if first_calories < lower:
                score-=1
        return score

        
#         score, cals = 0, sum(calories[0: k])
#         if cals > upper: 
#             score += 1
#         if cals < lower: 
#             score -= 1
        
#         for i in range(k,len(calories)):
#             cals = cals+calories[i]-calories[i-k]
#             if cals > upper: 
#                 score += 1
#             if cals < lower: 
#                 score -= 1
        
#         return score
