'''
Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.
'''

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        """
        input:
        0 - [l, g, f]
        1 - [g, m]
        2 - [g, f]
        3 - [g]
        4 - [a]
        
        fc_map {string:set}
        l - [0]
        g - [0, 1, 2, 3]
        f - [0, 2]
        m - [1]
        a - [4]
        
        
        person 0 - [l, g, f]:
        [0]
        [0, 1, 2, 3]
        [0, 2]
        [_3_, 1, 2, 1] <- accept: person 0 has most fc
        
        person 1 - [g, m]:
        [0, 1, 2, 3]
        [1]
        [1, _2_, 1, 1] <- accept: person 1 has most fc
        
        person 2 - [g, f]:
        [0, 1, 2, 3]
        [0, 2]
        [2, 1, _2_, 1] <- reject: person 0 has the same fc as person 2
        
        person 3 - [g]
        [0, 1, 2, 3]
        [1, 1, 1, _1_] <- reject: person 3 has the same fc as everyone
        """
        
        fc_map = {}
        for i in range(len(favoriteCompanies)):
            fcs = favoriteCompanies[i]
            for fc in fcs:
                if fc not in fc_map:
                    fc_map[fc] = set([i])
                else:
                    fc_map[fc].add(i)
                   
        print(fc_map)
        
        num_people = len(favoriteCompanies)
        result = []
        for i in range(len(favoriteCompanies)):
            fcs = favoriteCompanies[i]
            if self.goodness(fcs, fc_map, i, num_people):
                result.append(i)
                
        return result
    
    
    def goodness(self, fcs, fc_map, i, num_people) -> bool:
        counter = [0]*num_people
        
        for fc in fcs:
            ppl_idx_set = fc_map.get(fc)
            for idx in ppl_idx_set:
                counter[idx] += 1
                
        # check if counter[i] is greater than any other counter[i*]:
        c = counter[i]
        for ii in range(num_people):
            print(counter[i])
            if (ii != i) and (counter[ii] >= c):
                return False
            
        return True
----------------------------------------
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        for i in range(len(favoriteCompanies)):
            s = set(favoriteCompanies[i])
            flag = True
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                if s.issubset(set(favoriteCompanies[j])):
                    flag = False
                    break
            if flag:
                ans += [i]
        return ans
-------------------------------------------------------------------------------------
class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        res = set()
        l = len(favoriteCompanies)
        f = range(l)
        for i in range(l):
            for j in range(i + 1, l):
                a = self.find(f, i)
                b = self.find(f, j)
                if a == b:
                    continue
                elif self.contains(favoriteCompanies[a], favoriteCompanies[b]):
                    f[b] = f[a]
                elif self.contains(favoriteCompanies[b], favoriteCompanies[a]):
                    f[a] = f[b]
        
        for i in f:
            res.add(self.find(f, i))
        return sorted(res)
    
    def contains(self, a, b):
        if len(a) <= len(b):
            return False
        for i in b:
            if i not in a:
                return False
        return True
    
    def find(self, f, i):
        while f[i] != i:
            f[i] = f[f[i]]
            i = f[i]
        return i
      
