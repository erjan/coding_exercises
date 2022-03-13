'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If 
there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
'''

#my own solution

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = dict()
        d2 = dict()

        for i in range(len(list1)):
            d1[list1[i]] = i

        for i in range(len(list2)):
            d2[list2[i]] = i

        print(d1)
        print(d2)

        ind_sum = dict()
        for i in range(len(list1)):
            cur = list1[i]
            if cur in list2:
                ind_sum[cur] = d1[cur]
                ind_sum[cur] += d2[cur]
        print(ind_sum)

        min_sum = min(ind_sum.values())
        res = list()
        for k in ind_sum.keys():
            if ind_sum[k] == min_sum:
                res.append(k)
        print(res)
        return res
