class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_list(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        k %= len(nums)
        # reverse the whole list
        reverse_list(0, len(nums) - 1)
        
        # reverse again starting fromm k -> end and from begin -> k
        reverse_list(k, len(nums) - 1)
        reverse_list(0, k - 1)
        