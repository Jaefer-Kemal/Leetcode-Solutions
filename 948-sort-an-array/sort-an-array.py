class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergedArray(left, right):
            merged = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            while i < len(left):
                merged.append(left[i])
                i += 1
            
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        def mergeSort(nums):
            if len(nums) == 1:
                return [nums[0]]

            low = 0
            high = len(nums) - 1
            mid = (low + high) // 2

            left = mergeSort(nums[:mid + 1])
            right = mergeSort(nums[mid + 1: ])

            return mergedArray(left, right)

        return mergeSort(nums)