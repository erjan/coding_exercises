'''
LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.
'''

class Solution:
    # 668 ms, 99.52%. Time: O(NlogN). Space: O(N)
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def is_within_1hr(t1, t2):
            h1, m1 = t1.split(":")
            h2, m2 = t2.split(":")
            if int(h1) + 1 < int(h2): return False
            if h1 == h2: return True
            return m1 >= m2
        
        records = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            records[name].append(time)
        
        rv = []
        for person, record in records.items():
            record.sort()
			# Loop through 2 values at a time and check if they are within 1 hour.
            if any(is_within_1hr(t1, t2) for t1, t2 in zip(record, record[2:])):
                rv.append(person)
        return sorted(rv)
      
-------------------------------------------
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        key_time = {}
        for index, name in enumerate(keyName):
            key_time[name] = key_time.get(name, [])
            key_time[name].append(int(keyTime[index].replace(":", "")))
        ans = []
        for name, time_list in key_time.items():
            time_list.sort()
            n = len(time_list)
            for i in range(n-2):
                if time_list[i+2] - time_list[i] <= 100:
                    ans.append(name)
                    break
        return sorted(ans)
