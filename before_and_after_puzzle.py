'''

Given a list of phrases, generate a list of Before and After puzzles.

A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

Before and After puzzles are phrases that are formed by merging two phrases where the last word of the first phrase is the same as the first word of the second phrase.

Return the Before and After puzzles that can be formed by every two phrases phrases[i] and phrases[j] where i != j. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of distinct strings sorted lexicographically.

'''

def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        start = {}
        for i in range(len(phrases)):
            words = list(phrases[i].split(" "))
            sw,ew = words[0],words[-1]
            if sw in start:
                start[sw].append(i)
            else:
                start[sw] = [i]
            
            
        #print (start)
        res = []
        seen = set()
        for i in range(len(phrases)):
            ew = list(phrases[i].split(" "))[-1]    
            if ew in start:
                for j in start[ew]:
                    if i!=j:
                        string = phrases[i]+phrases[j][len(ew):]
                        if string in seen:
                            continue
                        else:
                            res.append(string)
                            seen.add(string)
        return sorted(res)**
      
--------------------------
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        first, last = defaultdict(Counter), defaultdict(Counter)
        for p in phrases:
            words = p.split()
            first[words[0]][p] += 1
            last[words[-1]][p] += 1
        ans = set()
        for w in first:
            for p1 in first[w]:
                for p2 in last[w]:
                    if p1 == p2 and first[w][p1] == 1:
                        continue
                    ans.add(p2[:-len(w)] + p1)
        return sorted(ans)
