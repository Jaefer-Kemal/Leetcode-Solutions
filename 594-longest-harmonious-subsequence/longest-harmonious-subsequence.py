class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count_freq = Counter(nums)
        longest = 0

        for num in nums:
            if num - 1 in count_freq:
                longest = max(longest, count_freq[num] + count_freq[num - 1])
        
        return longest