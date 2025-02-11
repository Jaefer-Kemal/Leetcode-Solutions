class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        maximum_element = max(nums) + 1
        count_arr = [0] * maximum_element

        for num in nums:
            count_arr[num] += 1
            
        index = 0
        for num in range(maximum_element):
            while count_arr[num] > 0:
                nums[index] = num
                count_arr[num] -= 1
                index += 1
        
        res = []
        for i in range(len(nums)):
            if nums[i] > target:
                break

            if nums[i] == target:
                res.append(i)
        
        return res

        