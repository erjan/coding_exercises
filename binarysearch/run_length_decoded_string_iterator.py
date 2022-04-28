'''
Given a run-length encoded lowercase alphabet string s, implement an iterator which is the decoded version of s:

next() polls the next element in the iterator
hasnext() which returns whether the next element exists
Constraints

n ≤ 100,000 where n is the number of calls to next and hasnext
'''


class RunLengthDecodedIterator:

    def helper(self,s):

        i = 0
        j = 0
        res = list()
        while i < len(s):
            j = i
            temp = ''
            while j < len(s) and s[j].isdigit():
                temp += s[j]
                j += 1

            res.append("".join(temp))
            i = j+1

        letters = list(filter(lambda x: not x.isdigit(), s))
        res = [int(i) for i in res]

        main = list(zip(letters, res))
        main = [list(i) for i in main]

        #del letters, res
        return main

    def __init__(self, s):
        self.main = self.helper(s)
       
    def next(self):

        if self.main[0][1] != 0:
            self.main[0][1] -= 1
            temp = self.main[0][0]
            if self.main[0][1] == 0:
                self.main.pop(0)
            return temp


        elif self.main[0][1] == 0:
            self.main.pop(0)
            if len(self.main) > 0:
                self.main[0][1] -= 1
                return self.main[0][0]
            return

    def hasnext(self):

        if len(self.main) > 0:
            return True
        return False
        
