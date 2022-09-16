'''
You are the operator of a Centennial Wheel that has four gondolas, and each gondola has room for up to four people. You have the ability to rotate the gondolas counterclockwise, which costs you runningCost dollars.

You are given an array customers of length n where customers[i] is the number of new customers arriving just before the ith rotation (0-indexed). This means you must rotate the wheel i times before the customers[i] customers arrive. You cannot make customers wait if there is room in the gondola. Each customer pays boardingCost dollars when they board on the gondola closest to the ground and will exit once that gondola reaches the ground again.

You can stop the wheel at any time, including before serving all customers. If you decide to stop serving customers, all subsequent rotations are free in order to get all the customers down safely. Note that if there are currently more than four customers waiting at the wheel, only four will board the gondola, and the rest will wait for the next rotation.

Return the minimum number of rotations you need to perform to maximize your profit. If there is no scenario where the profit is positive, return -1.
'''

class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        CAPACITY = 4
        NO_PROFIT = -1
        
        numCustomersWaiting = 0
        totalCustomers = 0

        currentProfit = NO_PROFIT
        previousProfit = NO_PROFIT
        maxProfit = NO_PROFIT
        
        numRotations = 0
        minRotationsForMaxProfit = NO_PROFIT
        
        while customers or numCustomersWaiting:
            
            # GET THE NEXT GROUP OF CUSTOMERS
            currentNumCustomers = customers.pop(0) if customers else 0
            
            # ADD TO TOTAL NUMBER OF CUSTOMERS WAITING
            numCustomersWaiting += currentNumCustomers 
            
            # BOARD THE NEXT GROUP, 4 IS THE CAPACITY
            numCustomersBoarding = min(numCustomersWaiting, CAPACITY)
            
            # REMOVE BOARDING GROUP FROM NUMBER OF CUSTOMERS WAITING
            numCustomersWaiting = numCustomersWaiting - numCustomersBoarding
                       
            # KEEP TOTAL COUNT OF CUSTOMERS TO CALCULATE PROFIT
            totalCustomers += numCustomersBoarding
            
            # ROTATE THE CENTENNIAL WHEEL
            numRotations += 1
            
            # CALCULATE CURRENT PROFIT
            currentProfit = (totalCustomers * boardingCost) - (numRotations * runningCost)
            
            # MAINTAIN HIGHEST PROFIT NUMBER FOR RETURN
            if 0 < currentProfit > maxProfit:
                maxProfit = currentProfit
                minRotationsForMaxProfit = numRotations
            
            # SET UP FOR NEXT ITERATION
            previousProfit = currentProfit
            
        return minRotationsForMaxProfit
-----------------------------------------------------

class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost: int, runningCost: int) -> int:
        profit = 0
        waiting = 0
        lst_profit = []
        for arrived in customers:
            waiting += arrived
            loading = min(4, waiting)
            waiting -= loading
            profit += loading * boardingCost - runningCost
            lst_profit.append(profit)
        while waiting:
            loading = min(4, waiting)
            waiting -= loading
            profit += loading * boardingCost - runningCost
            lst_profit.append(profit)
        max_profit = max(lst_profit)
        return lst_profit.index(max_profit) + 1 if max_profit > 0 else -1
