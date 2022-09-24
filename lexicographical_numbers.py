'''
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 
'''


class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
class Trie:
    def __init__(self):
        self.head=TrieNode()
    def add(self,val):
        curr=self.head
        for c in val:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.end=True
        
    def printall(self,curr,string,final):
        if(curr.end):
            final.append(string)
        for c in curr.children:
            string+=c
            self.printall(curr.children[c],string,final)
            string=string[:-1]
    def printme(self):
        final=[]
        self.printall(self.head,'',final)
        return final
            
        

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        t=Trie()
        for i in range(1,n+1):
            t.add(str(i))
        return([int(c) for c in t.printme()])
        
----------------------------------------------------------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False
        self.count = 0
        self.data = ''

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # we're using strings to insert into the trie
        nums = [str(x) for x in range(1, n+1)]
        root = TrieNode()
        
        # populate the trie with individual
        # letters in the string (num)
        for num in nums:
            digits = list(num)
            cur = root
            for digit in digits:
                if digit not in cur.children:
                    cur.children[digit] = TrieNode()
                cur = cur.children[digit]
            cur.end = True
            
            # for ever num node ending
            # store the num here itself
            cur.data = num
        
        res = []
        self.dfs(root, res)
        return [int(x) for x in res]
            
    # do a dfs on the root node
    def dfs(self, node, res):
        # if the current node is an end
        # node, this is a potential result
        # save it but keep progressing
        # because there might be another word
        # later on, on this same path
        # e.g. 10, 101
        if node.end:
            res.append(node.data)
        
        # any node can have their children
        # from 0-9 since we're only storing
        # digits in a node so iterate over
        # n -> 0,9 and recursively call dfs
        # if the current node has n as a child
        for n in range(10):
            if str(n) in node.children:
                self.dfs(node.children[str(n)], res)
