'''
You are given an array tasks where tasks[i] = [actuali, minimumi]:

actuali is the actual amount of energy you spend to finish the ith task.
minimumi is the minimum amount of energy you require to begin the ith task.
For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.

You can finish the tasks in any order you like.

Return the minimum initial amount of energy you will need to finish all the tasks.
'''

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: [x[0]-x[1],-x[1],x[0]])
        energy=0
        energyTotal=0
        for a,b in tasks:
            e=energy-b
            if e<0:
                energy-=e
                energyTotal-=e
            energy-=a
            
        return energyTotal
	```
