'''
You are given a string, message, and a positive integer, limit.

You must split message into one or more parts based on limit. Each resulting part should have the suffix "<a/b>", where "b" is to be replaced with the total number of parts and "a" is to be replaced with the index of the part, starting from 1 and going up to b. Additionally, the length of each resulting part (including its suffix) should be equal to limit, except for the last part whose length can be at most limit.

The resulting parts should be formed such that when their suffixes are removed and they are all concatenated in order, they should be equal to message. Also, the result should contain as few parts as possible.

Return the parts message would be split into as an array of strings. If it is impossible to split message as required, return an empty array.

 
 '''


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        best = math.inf
        def check(x):
            avail = 0
            start = 1
            while start <= x:
                next_start = start * 10
                suffix = f"<{start}/{x}>"
                if len(suffix) > limit:
                    return False
                avail += (min(next_start - 1, x) - start + 1) * (limit - len(suffix))
                start = next_start
            last_suffix = f"<{x}/{x}>"
            return avail >= n >= avail - (limit - len(last_suffix))
        
        for n_part in range(1, n + 1):
            if check(n_part):
                break
        else:
            return []
        
        ans = []
        start = 0
        for i in range(1, n_part + 1):
            suffix = f"<{i}/{n_part}>"
            next_start = start + limit - len(suffix)
            ans.append(message[start:next_start] + suffix)
            start = next_start
        return ans
        
        
        
