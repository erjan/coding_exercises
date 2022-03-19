'''
You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.

Return the array answer as described above.
'''


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        s = defaultdict(set)
        ids = list()
        for log in logs:

            uid = log[0]
            ids.append(uid)

        for log in logs:
            uid = log[0]
            min = log[1]

            if min not in s[uid]:
                s[uid].add(min)

        for i, v in s.items():
            s[i] = len(v)

        s = list(s.values())
        
        res = [0] * (k+1)
        print(res)
        q = dict(Counter(s))
        for j in range(1,  k+1):
            if j in q.keys():
                res[j] = q[j]

        res = res[1:]
        del q,s, ids,logs
        

        return res
