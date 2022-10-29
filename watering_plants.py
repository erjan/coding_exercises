'''
You want to water n plants in your garden with a watering can. The plants are arranged in a row and are labeled from 0 to n - 1 from left to right where the ith plant is located at x = i. There is a river at x = -1 that you can refill your watering can at.

Each plant needs a specific amount of water. You will water the plants in the following way:

Water the plants in order from left to right.
After watering the current plant, if you do not have enough water to completely water the next plant, return to the river to fully refill the watering can.
You cannot refill the watering can early.
You are initially at the river (i.e., x = -1). It takes one step to move one unit on the x-axis.

Given a 0-indexed integer array plants of n integers, where plants[i] is the amount of water the ith plant needs, and an integer capacity representing the watering can capacity, return the number of steps needed to water all the plants.
'''


--- Here we first store the value of capacity into x variable after that we work on the plants list and check for each index value , and if the can capacity x is less then the plant required value we add its travelling back and forth value to the count and decrease its current index value from the max capacity at the same time .

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        x=capacity
        count=0
        for i in range(len(plants)):
            if(x<plants[i]):
                count=count+i+i+1
                x=capacity-plants[i]
            
            else:
                count=count+1
                x=x-plants[i]
                  
        return(count)
