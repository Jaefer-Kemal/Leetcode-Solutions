class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_freq = defaultdict(int)
        maximum = float("-inf")
        majority_element = None
        for num in nums:
            count_freq[num] += 1
            if maximum < count_freq[num]:
                majority_element = num
                maximum = count_freq[num]
        
        return majority_element