class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_count = Counter(nums)

        count_freq = defaultdict(int)
        maximum_frequency = 0   
        for count in nums_count.values():
            count_freq[count] += 1
            if count > maximum_frequency:
                maximum_frequency = count
        
        res = maximum_frequency * count_freq[maximum_frequency]
        return res
