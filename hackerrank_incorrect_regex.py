'''
You are given a string .
Your task is to find out whether s is a valid regex or not.
'''

import re

if __name__ == '__main__':

    

    n = int(input())

    for _ in range(n):

        regex = input()
        try:
            status = True
            t = re.compile(regex)
            
        except re.error:
            status = False
            
        print(status)
     
