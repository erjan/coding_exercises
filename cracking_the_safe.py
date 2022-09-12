'''
There is a safe protected by a password. The password is a sequence of n digits where each digit can be in the range [0, k - 1].

The safe has a peculiar way of checking the password. When you enter in a sequence, it checks the most recent n digits that were entered each time you type a digit.

For example, the correct password is "345" and you enter in "012345":
After typing 0, the most recent 3 digits is "0", which is incorrect.
After typing 1, the most recent 3 digits is "01", which is incorrect.
After typing 2, the most recent 3 digits is "012", which is incorrect.
After typing 3, the most recent 3 digits is "123", which is incorrect.
After typing 4, the most recent 3 digits is "234", which is incorrect.
After typing 5, the most recent 3 digits is "345", which is correct and the safe unlocks.
Return any string of minimum length that will unlock the safe at some point of entering it.
'''


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        self.ans=None
        self.visited=set()
        def backtrack(curr):
            # print(curr,self.visited)
            if len(self.visited)==k**n:
                self.ans=curr
                return True
            
            for i in range(k):
                new_curr=str(i)+curr
                if new_curr[:n] not in self.visited:
                    self.visited.add(new_curr[:n])
                    if backtrack(new_curr):
                        return True
                    self.visited.remove(new_curr[:n])
            return False
        backtrack('0'*(n-1))
        return self.ans
