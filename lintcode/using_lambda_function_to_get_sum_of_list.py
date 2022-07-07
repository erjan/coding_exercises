'''
Please complete the 
code in solution.py to realize the function 
of get_sum. get_sum function receives an array parameter nums. Please use 
the lambda function to pass in two unknown number x and y for the get_sum 
function and take this lambda function as the return value of the get_sum 
function. For the parameter nums received by get_sum, if the length of the
array num is an even number, return the sum of nums by x times. If the length
of the array num is an odd number, return the sum of nums by -y times.

'''
def get_sum(nums: list):
    # Write your code here.

    if len(nums) %2 == 0:
        even = True
    else:
        even = False
    s = sum(nums)
    return lambda x,y :  s*x if even else -y*s
