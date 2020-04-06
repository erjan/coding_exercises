#medium problem
'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''


from collections import defaultdict

def f(a):
    res = defaultdict(list)
    for i in a:
        temp = ''.join(sorted(i))
        if temp in res:
            res[temp].append(i)
        else:
            res[temp] = [i]
            
    res =list(res.values())
    return res
    for k in res:
        print(k)


a = ["eat", "tea", "tan", "ate", "nat", "bat"]
f(a)
