'''
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.

 
 '''

Explanation
Any idea = first letter + postfix string.
We can group all ideas by their first letter.

If two ideas ideas[i] and ideas[j] share a common postfix string,
then ideas[i] can not pair with any idea starts with ideas[j][0]
and ideas[j] can not pair with any idea starts with ideas[i][0].

    def distinctNames(self, ideas):
        count = defaultdict(set)
        for a in ideas:
            count[a[0]].add(hash(a[1:]))
        res = 0
        for a, seta in count.items():
            for b, setb in count.items():
                if a >= b: continue
                same = len(seta & setb)
                res += (len(seta) - same) * (len(setb) - same)
        return res * 2
      
---------------------------------------------------------
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ss = [set() for _ in range(26)]
        for s in ideas:
            c = ord(s[0]) - ord('a')
            tail = s[1:]
            ss[c].add(tail)

        ans = 0
        for i in range(26):
            for j in range(26):
                if i == j: continue
                a = len(ss[i] - ss[j])
                b = len(ss[j] - ss[i])
                ans += a * b
        return ans


true, false, null = True, False, None
cases = [
    (["coffee", "donuts", "time", "toffee"], 6),
    (["lack", "back"], 0),
]
