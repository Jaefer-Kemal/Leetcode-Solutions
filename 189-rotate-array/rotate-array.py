class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1

        n = len(nums)
        k %= n
        if k == 0:
            return

        # reverse the entire array
        reverse(nums,0, n - 1)

        # reverse from 0 to k - 1
        reverse(nums,0, k - 1)

        # reverse from k to n - 1
        reverse(nums,k , n - 1)

        