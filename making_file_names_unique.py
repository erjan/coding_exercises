'''
Given an array of strings names of size n. You will create n folders in your file system such that, at the ith minute, you will create a folder with the name names[i].

Since two files cannot have the same name, if you enter a folder name that was previously used, the system will have a suffix addition to its name in the form of (k), where, k is the smallest positive integer such that the obtained name remains unique.

Return an array of strings of length n where ans[i] is the actual name the system will assign to the ith folder when you create it.
'''

  from collections import defaultdict
    def getFolderNames(self, names: List[str]) -> List[str]:
        used, hashmap = set(), defaultdict(int)
        result = []
        for name in names:
            k = hashmap[name]
            current = name
            while current in used:
                k += 1
                current = '%s(%d)' % (name, k)  # alternative to current = name+'('+str(k)+')'
            hashmap[name] = k
            result.append(current)
            used.add(current)
        return result
      
-------------------------------------------------------------
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = {}
        arr = []
        for i in range(len(names)):
            if names[i] not in seen:
                seen[names[i]] = 1
                arr.append(names[i])
            else:
                n = seen[names[i]]
                new_name = names[i] + "(" + str(n) + ")"
                while new_name in seen:
                    n += 1
                    new_name = names[i] + "(" + str(n) + ")"
                arr.append(new_name)
                seen[names[i]] += 1
                seen[new_name] = 1
        
        return arr
