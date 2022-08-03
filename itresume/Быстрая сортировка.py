
'''
Реализуйте сортировку массива методом быстрой сортировки.
'''

class Answer:
    
        
    def quick_sort(self, nums):
        def partition(nums, start, end):
            pivot = nums[start]
            low = start + 1
            high = end

            while True:
        
                while low <= high and nums[high] >= pivot:
                    high = high - 1

        # Opposite process of the one above
                while low <= high and nums[low] <= pivot:
                    low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
                if low <= high:
                    nums[low], nums[high] = nums[high], nums[low]
            # The loop continues
                else:
            # We exit out of the loop
                    break

            nums[start], nums[high] = nums[high], nums[start]

            return high
    
        def q(array, begin, end):
            if begin >= end:
                return
            pivot = partition(array, begin, end)
            q(array, begin, pivot-1)
            q(array, pivot+1, end)
        
        
        return q(nums, 0, len(nums) - 1)
