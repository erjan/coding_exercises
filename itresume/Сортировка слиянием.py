class Answer:
    def merge_sort(self, nums):
                
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            # Recursive call on each half
            self.merge_sort(left)
            self.merge_sort(right)

            # Two iterators for traversing the two halves
            i = 0
            j = 0

            # Iterator for the main list
            k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    # The value from the left half has been used
                    nums[k] = left[i]
                # Move the iterator forward
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
        return nums
