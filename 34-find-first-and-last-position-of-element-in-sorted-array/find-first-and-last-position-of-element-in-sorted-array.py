class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def findRight(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        start = findLeft(nums, target)
        end = findRight(nums, target)

        if start <= end and start < len(nums) and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]
