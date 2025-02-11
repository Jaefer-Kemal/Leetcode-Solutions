class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums_count = defaultdict(int)

        maximum_element = max(nums) + 1
        minimum_element = min(nums)
        
        for i in range(len(nums)):
            nums_count[nums[i]] += 1

        i = 0
        for num in range(minimum_element, maximum_element):
            while nums_count[num] > 0:
                nums[i] = num
                nums_count[num] -= 1
                i += 1

        return nums