'''
You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.
'''

from sortedcontainers import SortedList

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        sl = SortedList()
        length = SortedList()
        curr = 0
        for char, it in itertools.groupby(s):
            c = sum(1 for _ in it)
            length.add(c)
            sl.add((curr, curr + c, char))
            curr += c
        ans = []
        for char, i in zip(queryCharacters, queryIndices):
            t = (i, math.inf, 'a')
            index = sl.bisect_right(t) - 1
            to_remove = [sl[index]]
            to_add = []
            left, right, original_char = to_remove[0]
            if original_char != char:
                length.remove(right - left)
                if right - left > 1:
                    if i == left:
                        left += 1
                        to_add.append((left, right, original_char))
                        length.add(right - left)
                    elif i == right - 1:
                        right -= 1
                        to_add.append((left, right, original_char))
                        length.add(right - left)
                    else:
                        to_add.append((left, i, original_char))
                        length.add(i - left)
                        to_add.append((i + 1, right, original_char))
                        length.add(right - (i + 1))
                
                l, r = i, i + 1
                if index - 1 >= 0 and sl[index - 1][1:3] == (i, char):
                    l, old_r, _ = sl[index - 1]
                    to_remove.append(sl[index - 1])
                    length.remove(old_r - l)
                if index + 1 < len(sl) and sl[index + 1][0] == i + 1 and sl[index + 1][2] == char:
                    old_l, r, old_length = sl[index + 1]
                    to_remove.append(sl[index + 1])
                    length.remove(r - old_l)
                length.add(r - l)
                sl.add((l, r, char))
                for t in to_remove:
                    sl.remove(t)
                sl.update(to_add)
            # print(sl)
            # print(length)
            ans.append(length[-1])

        return ans
      
--------------------------------------------------------------------------------------------
from collections import defaultdict
from sortedcontainers import SortedList

    
class Dummy:
    def __init__(self, idx):
        self.r = idx
        
class Node:
    maxL = None
    crtMaxL = 0
    def __init__(self, l, r, chr):
        self.l, self.r, self.c, self.length = l, r, chr, r - l
        self.add()
        
    def update(self, new_l, new_r):
        self.l, self.r, self.length = new_l, new_r, new_r - new_l
        self.add()
        
    def add(self):
        Node.maxL[self.length] += 1
        if self.length > Node.crtMaxL:
            Node.crtMaxL = self.length
    
    def remove(self):
        Node.maxL[self.length] -= 1
        if Node.maxL[self.length] == 0:
            del Node.maxL[self.length]
            if self.length == Node.crtMaxL:
                Node.crtMaxL = max(Node.maxL.keys(), default=0)

    def split(self, idx, c):
        self.remove()
        ret = []
        if self.l < idx:
            ret.append(Node(self.l, idx - 1, self.c))
        ret.append(Node(idx, idx, c))
        if self.r > idx:
            ret.append(Node(idx + 1, self.r, self.c))
        return self.l == idx, self.r == idx, ret

    def merge(nodes):
        i = 0
        ret = []
        while i < len(nodes):
            l = i
            while i < len(nodes) and nodes[l].c == nodes[i].c:
                nodes[i].remove()
                i += 1
            nodes[l].update(nodes[l].l, nodes[i - 1].r)
            ret.append(nodes[l])
        return ret
            
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        nodes = []
        Node.maxL = defaultdict(int)
        Node.crtMaxL = 0
        ret = []
        i = 0
        while i < len(s):
            l = i
            while i < len(s) and s[i] == s[l]:
                i += 1
            node = Node(l, i - 1, s[l])
            nodes.append(node)
            
        nodes = SortedList(nodes, key=lambda x:x.r)
        
        def update_nodes(idx, c):
            nonlocal nodes
            i = nodes.bisect_left(Dummy(idx))
            node = nodes[i]
            if c == node.c:
                return
            
            need_merge_left, need_merge_right, list_of_nodes = node.split(idx, c)
            
            list_to_remove = [node]
            list_to_merge = []
            if need_merge_left and i > 0 and nodes[i - 1].c == c:
                lNode = nodes[i - 1]
                list_to_merge.append(lNode)
                list_to_remove.append(lNode)
            
            list_to_merge += list_of_nodes
            
            if need_merge_right and i < len(nodes) - 1 and nodes[i + 1].c == c:
                rNode = nodes[i + 1]
                list_to_merge.append(rNode)
                list_to_remove.append(rNode)
                
            [nodes.remove(n) for n in list_to_remove]
            nodes.update(Node.merge(list_to_merge))
                
        for c, idx in zip(queryCharacters, queryIndices):
            update_nodes(idx, c)
            ret.append(Node.crtMaxL + 1)

        return ret
