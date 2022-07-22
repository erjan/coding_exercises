
'''
You are given a 0-indexed 2D integer array brackets where brackets[i] = [upperi, percenti] means that the ith tax bracket has an upper bound of upperi and is taxed at a rate of percenti. The brackets are sorted by upper bound (i.e. upperi-1 < upperi for 0 < i < brackets.length).

Tax is calculated as follows:

The first upper0 dollars earned are taxed at a rate of percent0.
The next upper1 - upper0 dollars earned are taxed at a rate of percent1.
The next upper2 - upper1 dollars earned are taxed at a rate of percent2.
And so on.
You are given an integer income representing the amount of money you earned. Return the amount of money that you have to pay in taxes. Answers within 10-5 of the actual answer will be accepted.
'''

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income == 0:
            return 0.0

        prev = 0
        total_tax = 0
        for k, v in brackets:
            k = min(k,income)
            total_tax += (k - prev)*v/100
            prev = k
            
        return total_tax

    
-------------------------------------------------------------------------------

Zewei_Liu's avatar
Zewei_Liu
0
June 14, 2022 6:23 PM

27 VIEWS

This problem could be solved with 2-step approach.

Spliting income to each tax bracket.
Calculating tax in each income split.
Simple Python3 code below:

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        tax = 0 
        pre_upper = 0
        for tax_bracket in brackets:
            upper = tax_bracket[0]
            percent = tax_bracket[1]
            split_income = upper - pre_upper if income >= upper else income - pre_upper
            tax += split_income * percent * 0.01
            if income < upper:
                break
            pre_upper = upper
        
        return tax
    
----------------------------------------------------------------------------------------------
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        lower = 0; 
		tax = 0; 
		left = income # amount left to be taxed
        for i in brackets:
            k = i[0]-lower # amount being taxed
            if k<= left:
                tax+=k*i[1]/100;  left-=k;  lower=i[0]
            else:
                tax+= left*i[1]/100
                break
        return tax

--------------------------------------------------
class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        cur, res = 0, 0
        for upper, percent in brackets:
            pre, cur = cur, min(upper, income)
            res += (cur - pre) * percent
        return res / 100
