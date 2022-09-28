'''
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
'''


#this takes lots of space though
class SnapshotArray:
    def __init__(self, length: int):
        self.cache = []
        self.d = dict()
        self.i = 0

    def set(self, index: int, val: int) -> None:
        self.d[index] = val

    def snap(self) -> int:
        self.cache.append(dict(self.d))
        self.i += 1
        return self.i-1

    def get(self, index: int, snap_id: int) -> int:
        snap = self.cache[snap_id]
        return snap[index] if index in snap else 0
----------------------------------------------------------------------------------------------------------      

class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.list = [[[-1, 0]] for _ in range(length)]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        
        self.list[index].append([self.snap_id, val])
        
    def snap(self):
        """
        :rtype: int
        """
        ans = self.snap_id
        self.snap_id += 1
        return ans
    
    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        #print(self.list)
        li = self.list[index]
        left, right = 0, len(li) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if li[mid][0] <= snap_id:
                left = mid
            else:
                right = mid
        if li[right][0] <= snap_id:
            return li[right][1]
        return li[left][1]
