class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        maximum_limit = 10 ** 9 + 7
        
        nums.sort(reverse = True)
        max_len = len(nums) 
        intervals = [0] * (max_len + 1)

        for start, end in requests:
            intervals[start] += 1
            intervals[end + 1] -= 1
        
        for i in range(1, max_len + 1):
            intervals[i] += intervals[i - 1]
        
        intervals.sort(reverse = True)
        
        max_sum = 0
        for i in range(max_len):
            if intervals[i] != 0:
                max_sum += (intervals[i] * nums[i])
            else:
                break
        
        return max_sum % maximum_limit