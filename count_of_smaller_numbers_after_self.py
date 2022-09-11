	'''
  Given an integer array nums, return an integer 
  array counts where counts[i] is the number of smaller elements to the right of nums[i].
  '''
  
  def countSmaller(self, nums: List[int]) -> List[int]:
        
        res  = [0] * len(nums)                                    # NOTE 1
        enum = list(enumerate(nums))                              # NOTE 2
        
        self.mergeSort(enum, 0, len(nums) - 1, res)
        return res
    
    def mergeSort(self, enum, start, end, res):
        if start >= end: return
        
        mid = start + (end - start) // 2
        self.mergeSort(enum, start, mid, res)
        self.mergeSort(enum, mid + 1, end, res)
        self.merge(enum, start, mid, end, res)
    
    def merge(self, enum, start, mid, end, res):
        p, q = start, mid + 1
        inversion_count = 0                                      # NOTE 3
        temp = []
        
        while p <= mid and q <= end:
            if enum[p][1] <= enum[q][1]:
                temp.append(enum[p])
                res[enum[p][0]] += inversion_count               # NOTE 5
                p += 1
            else:
                temp.append(enum[q])
                inversion_count += 1                             # NOTE 4
                q += 1
        
        while p <= mid:
            temp.append(enum[p])
            res[enum[p][0]] += inversion_count                  # NOTE 6
            p += 1
        
        while q <= end:         
            temp.append(enum[q])
            q += 1
        
        enum[start:end+1] = temp             
--------------------------------------------------------------------------------------
def countSmaller(self, nums):
    rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
    BITree = [0] * (N + 1)
    
    def update(i):
        while i <= N:
            BITree[i] += 1
            i += (i & -i)
        
    def getSum(i):
        s = 0
        while i:
            s += BITree[i]
            i -= (i & -i)
        return s
    
    for x in reversed(nums):
        res += getSum(rank[x] - 1),
        update(rank[x])
    return res[::-1]
