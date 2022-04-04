
'''

In this question, we will provide two lists list_1 and list_2. We have already declared the list_expression function for you in solution.py. The list_1 and list_2 of this function represent the initial list. Need to comprehend by list:

Multiply each value in the two lists separately
Add each value in the two lists separately
Multiply the values in the two lists
'''

def list_expression(list_1: list, list_2: list):
    '''
    :param list_1: Input list_1
    :param list_2: Input list_2
    :return: nothing
    '''
    # -- write your code here --

    n1 = list_1
    n2 = list_2
    res = [i*j for i in n1 for j in n2]
    print(res)

    res = [i+j for i in n1 for j in n2]
    print(res)

    res = [a * b for a, b in zip(n1, n2)]
    print(res)
