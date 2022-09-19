'''
You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.
'''


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        running = 0
        for roll in rolls: #count the running total of all known dice rolls
            running += roll
        total_rolls = len(rolls) + n
        #calculate sum of missing values
        total_missing = (mean * total_rolls) - running
        #check for edge cases in which the average roll would need to be outside 
        #of possible dice rolls 
        if total_missing / n < 1 or total_missing / n > 6:
            return []
        #most of the time, this will be the most common value of the remaining rolls
        most_rolls = total_missing // n
        output = [most_rolls] * (n-1)
        #at this point, we have one remaining roll 
        total_missing -= (most_rolls * (n-1))
        #per problem constraints, the maximum value we can roll is a 6
        last_val = min(6, total_missing)
        output.append(last_val)
        total_missing -= last_val
        idx = 0
        #if rolling a 6 (or lower) does not solve problem, update remaining 
        #rolls to cause the average dice roll to equal mean input variable
        while total_missing > 0:
            total_missing += output[idx]
            last_val = min(6, total_missing)
            output[idx] = last_val
            total_missing -= last_val
            idx +=1
        return output
