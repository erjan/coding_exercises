'''
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.
'''


from typing import List
from collections import Counter


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Basic idea is to find the most common number in both the top and bottom rows. If all dominoes contain
        that most common number at least once then return the smallest number of spaces out of the top or bottom row which will
        be the fewest number of rotations we need to do.
        """
        value, count = Counter(tops + bottoms).most_common()[0]
        for t, b in zip(tops, bottoms):
            if t != value and b != value:
                # if neither the top or bottom of a single domino contain the most common element
				# then the target condition can never be achieved
                return -1
        if count >= len(tops):
            return min([len(tops) - tops.count(value), len(bottoms) - bottoms.count(value)])
        return -1



--------------------------------------------------------------------------------------------------------------------------------------------


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        top_freq = dict(Counter(tops))
        bottom_freq = dict(Counter(bottoms))

        most_frequent_top = [[k,v] for k,v in top_freq.items()]
        most_frequent_top.sort(key = lambda x: x[1], reverse=True)

        most_frequent_bottom = [[k,v] for k,v in bottom_freq.items()]
        most_frequent_bottom.sort(key = lambda x: x[1], reverse=True)

        n = len(tops)
        most_frequent_top = most_frequent_top[0]
        most_frequent_bottom = most_frequent_bottom[0]

        print(top_freq)
        print(bottom_freq)
        print('-----------')

        print('most top val')
        most_frequent_top_number = most_frequent_top[0]
        most_frequent_bottom_number = most_frequent_bottom[0]

        print(f'most_frequent top number: {most_frequent_top_number}')        
        print(f'most_frequent bottom number: {most_frequent_bottom_number}')

        most_frequent_top_number_count = most_frequent_top[1]
        most_frequent_bottom_number_count = most_frequent_bottom[1]





        res1 = res2 = 0

        m = list(zip(tops,bottoms))
        #make all tops same

        newtops = []
        for t,b in m:
                if t!= most_frequent_top_number:
                        if bottom_freq[most_frequent_bottom_number]>0:
                                bottom_freq[most_frequent_bottom_number]-=1
                                newtops.append(b)
                                res1+=1
                else:
                        newtops.append(t)
        
        print(f'newtops: {newtops}')
        expected_tops = [ most_frequent_top_number for x in  tops]
        print(f'expected tops: {expected_tops}')
        print('---------------')
        print('---------------')
        print('---------------')



        newbottoms = []
        for t,b in m:
                if b!= most_frequent_bottom_number:
                        if top_freq[most_frequent_top_number]>0:
                                top_freq[most_frequent_top_number]-=1
                                newbottoms.append(t)
                                res2+=1
                else:
                        newbottoms.append(b)
        
      
        expected_bottoms = [most_frequent_bottom_number for x in tops]
        print(f'newtops: {newtops}')
        print(f'newbottoms: {newbottoms}')
        print(f'expected: {expected_bottoms}')

        print(res1,res2)

        if newtops != expected_tops and  newbottoms != expected_bottoms:
                print('cant make newtops or newbottoms as expected')
                return -1
        

        print(min(res1,res2))
        return min(res1,res2)
       
