
'''
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) that tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.
'''


'''
For each a and b, if a knows b, then a can't be the celbrity and if a does not know b, then b can't be the celebrity. We check this for two adjacent values in the list and accordingly delete the value that can't be the celebrity from the list until the list is empty or has only one number in it, where that number can be the celebrity but we need to double check it.

There are occasions that there is one number left in the list, only because there is a loop in the graph, and we have only checked this graph in one direction. This is why we need to make sure that the remaining number is in fact the celbrity. So we check every node against it by asking knows(i, potential_celebrity), if there is a node that does not know the celebrity, then return -1. Also if there is a node that the potential_celebrity knows it, then this potential_celebrity is not the actual one and return -1 since there is no celebrity in the graoup.

In the big picture, the first phase, gets the potentail celebrity and the second phase double checks it.
'''

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        possibles = [i for i in range(n)]
        
        while len(possibles) > 1:
            #print(possibles)
            a = possibles.pop(0)
            b = possibles.pop(0)
            #print('a is {} and b is {}'.format(a,b))
            if knows(a,b):
                possibles.append(b)
            else:
                possibles.append(a)
        
        if len(possibles) == 1:
            val = possibles.pop()
            possibles.append(val)
            for i in range(n):
                if i!=val and (not knows(i,val) or knows(val,i)):
                    return -1
			return val
            
        return -1
      
------------------------------------------------
class Solution:
    def findCelebrity(self, n: int) -> int:

        ## RC ##
        ## APPROACH : GREEDY ##
        ## LOGIC : if i knows j then I is not celebrity and even if j doesn't know I then i is not celebrity ##
        
        isCelebrity = [True] * n
        for i in range(n):
            if isCelebrity[i]:
                for j in range(n):
                    if j != i and (knows(i, j) or not knows(j, i)):
                        isCelebrity[i] = False
                        break
                if isCelebrity[i]:
                    return i
        return -1
      
      --------------------------------------------------------------------------------
      class Solution:
    def findCelebrity(self, n: int) -> int:
        
        # Find a possible celebrity candidate,
        # if a candidate know any other member
        # he/she can't be a celebrity, but
        # the member they know can be then
        # considered as celebrity candidate
        candidate = 0
        for member in range(n):
            if knows(candidate, member):
                candidate = member
        
        # Check if candidate select doesn't know any other member
        # and the member must know the canidate, else return -1
        for member in range(n):
            # Check: member is not itself the candidate
            # Check: if candidate knows the member or if member doesn't know the candidate
            if member != candidate and (knows(candidate, member) or not knows(member, candidate)):
                return -1
        
        return candidate
