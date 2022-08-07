
'''
You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:

items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
The value of each item in items is unique.
Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.

Note: ret should be returned in ascending order by value.
'''
#my own solution

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        ret = list()

        if len(items1) >= len(items2):
            items1, items2 = items2, items1

        items1 = dict(items1)
        items2 = dict(items2)

        for v, w in items1.items():
            if v in items2:
                temp = [v, items2[v] + w]
                ret.append(temp)
            else:
                ret.append([v, w])

        ret = dict(ret)
        for v, w in items2.items():
            print(v, w)
            if v not in items1 and v not in ret:
                ret[v] = w
        ret = list([v, w] for v, w in ret.items())


        ret = sorted(ret, key=lambda x: x[0])
        return ret
      
------------------------------------------------------------------------------

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        
        hashset = {}

        for i in range(len(items1)):
            if items1[i][0] in hashset:
                hashset[items1[i][0]] += items1[i][1]
            else:
                hashset[items1[i][0]] = items1[i][1]

        for i in range(len(items2)):
            if items2[i][0] in hashset:
                hashset[items2[i][0]] += items2[i][1]
            else:
                hashset[items2[i][0]] = items2[i][1]
        
        ans = []

        for i in sorted(hashset):
            ans.append([i, hashset[i]])
        
        return ans      
