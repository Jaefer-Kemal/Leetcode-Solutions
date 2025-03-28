class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerBound(low, high):
            first = -1
            
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] >= target:
                    high = mid - 1
                    if nums[mid] == target:
                        first = mid
                else:
                    low = mid + 1
            
            return first
            
        def  upperBound(low, high):
            last = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] <= target:
                    low = mid + 1

                    if nums[mid] == target:
                        last = mid
                else:
                    high = mid - 1
            
            return last

        first = lowerBound(0, len(nums) - 1)
        last = upperBound(0, len(nums) - 1)

        return [first, last]