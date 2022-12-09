'''
There is a donuts shop that bakes donuts in batches of batchSize. They have a rule where they must serve all of the donuts of a batch before serving any donuts of the next batch. You are given an integer batchSize and an integer array groups, where groups[i] denotes that there is a group of groups[i] customers that will visit the shop. Each customer will get exactly one donut.

When a group visits the shop, all customers of the group must be served before serving any of the following groups. A group will be happy if they all get fresh donuts. That is, the first customer of the group does not receive a donut that was left over from the previous group.

You can freely rearrange the ordering of the groups. Return the maximum possible number of happy groups after rearranging the groups.
'''

    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        @cache
        def dp(counter_tup,mod):
            if sum(counter_tup)==0:
                return 0
            counter=list(counter_tup)
            startNewBatch = (mod==0)
            res = 0
            for i in range(len(counter)):
                if counter[i]!=0:
                    counter[i]-=1
                    mod2 = (mod-i)%batchSize
                    nxt_res = dp(tuple(counter),mod2) + startNewBatch
                    res = max(res, nxt_res)
                    counter[i]+=1
            return res
        counter = [0]*batchSize
        for g in groups:
            counter[g%batchSize]+=1
        return dp(tuple(counter),0)
      
------------------------------------------------------------------------------------------------------
class Solution:
    def maxHappyGroups(self, bs: int, gs: List[int]) -> int:
        c = {i: 0 for i in range(bs)}
        for g in gs:
            c[g % bs] += 1
        ret = c[0]
        c[0] = 0
        
        
        def get_keys(num):
            keys = []
            def rec(stack):
                if len(stack) == num:
                    if sum(stack) % bs == 0:
                        keys.append(Counter(stack))
                else:
                    for i in range(stack[-1] if stack else bs - 1, - 1, - 1):
                        stack.append(i)
                        rec(stack)
                        stack.pop()
            rec([])
            return keys
        
        def get_diff_keys(num):
            keys = []
            def rec(stack):
                if len(stack) == num:
                    if sum(stack) % bs == 0:
                        keys.append(Counter(stack))
                else:
                    for i in range(stack[-1] - 1 if stack else bs - 1, - 1, - 1):
                        stack.append(i)
                        rec(stack)
                        stack.pop()
            rec([])
            return keys
        
        for tc in range(2, bs):
            for keys in get_diff_keys(tc):
                add = min(c[key] // keys[key] for key in keys)
                if add == 0: continue
                ret += add
                for key in keys:
                    c[key] -= add * keys[key]
        tc = 2
        while True:
            for keys in get_keys(tc):
                add = min(c[key] // keys[key] for key in keys)
                if add == 0: continue
                ret += add
                for key in keys:
                    c[key] -= add * keys[key]
            if tc > sum(c.values()): break
            tc += 1
        return ret + bool(sum(c.values()))
