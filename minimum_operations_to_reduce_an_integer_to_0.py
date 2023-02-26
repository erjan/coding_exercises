Here's the plan:

We determine the binary string fornandsplitit on the zeros.
Wemapthe elements in thesplitlist to theirlenintegers.
If the mapped element is one, we incrementansby one (the subtract option); if greater than one, we incrementansas well as the next element by one as a carry digit (the add option).
There are a few other wrinkles, but that's the gist of it.

class Solution:
    def minOperations(self, n: int) -> int: # Example: n = 883 = 0b_1101110011
                                           
        n, ans = bin(n)[2:].split('0'), 0   #          n = ['11', '111','','11']
        
        n = list(map(len,n))+[0]            #          n = [  2 ,    3 , 0,  2 ] + [0]

        for i in range(len(n)-1):           #    i    ans     n            
            if n[i]:                        #   –––   –––     –––––––––
                ans+= 1                     #                 [2,3,0,2,0]
                n[i+1]+= n[i] > 1           #    0     1      [_,4,0,2,0]
                                            #    1     2      [_,_,1,2,0]
        return ans + n[-1]                  #    2     3      [_,_,_,2,0]
                                            #    3     4      [_,_,_,_,1]
                                            # return 4 + 1 = 5
