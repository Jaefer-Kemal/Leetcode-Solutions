class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_freq = defaultdict(int)
        max_count = len(nums) // 2
        for num in nums:
            count_freq[num] += 1
            if count_freq[num] > max_count:
                return num
            
        
        return majority_element