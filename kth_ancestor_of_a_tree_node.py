'''
You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of ith node. The root of the tree is node 0. Find the kth ancestor of a given node.

The kth ancestor of a tree node is the kth node in the path from that node to the root node.

Implement the TreeAncestor class:

TreeAncestor(int n, int[] parent) Initializes the object with the number of nodes in the tree and the parent array.
int getKthAncestor(int node, int k) return the kth ancestor of the given node node. If there is no such ancestor, return -1.
'''

class TreeAncestor(object):

    def __init__(self, n, parent):
        self.pars = [parent]
        self.n = n
        for k in range(17):
            row = []
            for i in range(n):
                p = self.pars[-1][i]
                if p != -1:
                    p = self.pars[-1][p]
                row.append(p)
            self.pars.append(row)
        

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        i = 0
        while k:
            if node == -1: 
				break
            if (k&1):
                node = self.pars[i][node]
            i += 1
            k >>= 1
        return node
      
---------------------------------------------------------------------------------------------------------------
