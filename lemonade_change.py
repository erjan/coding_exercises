'''
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        fives = list()
        tens = list()
        for i in range(len(bills)):
            if bills[i] == 5:
                fives.append(5)

            elif bills[i] == 10:              
                tens.append(10) 
                if len(fives) > 0:
                    
                    fives.pop()
                else:
                    return False
            elif len(tens) > 0:
                tens.pop()
                if len(fives) > 0:
                    fives.pop()
                else:
                    return False
            else:
                if len(fives) > 2:
                    fives.pop()
                    fives.pop()
                    fives.pop()
                else:
                    return False
            if len(fives) < 0:
                return False
        return True
                
     
