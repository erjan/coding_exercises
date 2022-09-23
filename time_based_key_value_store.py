'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
'''


class TimeMap(object):

    def __init__(self):
        self.map = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.map[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        values = self.map[key]
        if not values: return ''
        left, right = 0, len(values) - 1
        while left < right:
            mid = (left + right + 1) / 2
            pre_time, value = values[mid]
            if pre_time > timestamp:
                right = mid - 1
            else:
                left = mid
        return values[left][1] if values[left][0] <= timestamp else ''
