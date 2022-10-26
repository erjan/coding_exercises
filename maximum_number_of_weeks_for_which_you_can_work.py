'''
There are n projects numbered from 0 to n - 1. You are given an integer array milestones where each milestones[i] denotes the number of milestones the ith project has.

You can work on the projects following these two rules:

Every week, you will finish exactly one milestone of one project. You must work every week.
You cannot work on two milestones from the same project for two consecutive weeks.
Once all the milestones of all the projects are finished, or if the only milestones that you can work on will cause you to violate the above rules, you will stop working. Note that you may not be able to finish every project's milestones due to these constraints.

Return the maximum number of weeks you would be able to work on the projects without violating the rules mentioned above.
'''
------------------------------------------------------------
def numberOfWeeks(self, milestones: List[int]) -> int:
    #if the rules are not violated then u must have finished every milestone
    #if u finished every milestone then it must have taken sum(milestones) weeks
    #so the important question is how long it takes when you dont finish every milestone?
    
    #eg [3,1,1], in this case 3 cant be any larger if u want to finish every miletsone
    #eg [4,1,1], in this case 4 is just large enough that u cant finish every milestone
    #if max > sum - max + 1, then u cant finish every milestone
    #sum - max + 1 is how much u can reduce max value by
    #so total milestones completed = sum - max + 1 + (sum - max: rest of the element which are now 0)
    Max = max(milestones)
    Sum = sum(milestones)
    if 2*Max > Sum + 1:
        return 2*(Sum - Max) + 1
    
    return Sum
  
---------------------------------------------------------------------------------------------------------------------------------------
This problem is to put milestones in optimal order while keeping the non-consecutive milestone rule.

To keep milestones from being consecutive, we need to put milestones from other project in between them.

Let's say project with most milestones(P_i) have k milestones.
We need at least k -1 milestones to fill every gap between milestones.
Otherwise, milestones would be placed consecutively.

drawing

Since P_i has most milestones, rest of Project's milestones can be placed one by one in between P_i's milestones without considering their orders.

drawing

Therefore, the only case we need to care is when sum of rest of Projects' milestones is smaller than than the number of gaps(k - 1) between P_i's milestones.

Implementation

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
	    total_sum = sum(milestones)
        max_value = max(milestones)
        rest_sum = total_sum - max_value

        if max_value -1 > rest_sum:
            return total_sum - (max_value - 1 - rest_sum)
        return total_sum
  
  
