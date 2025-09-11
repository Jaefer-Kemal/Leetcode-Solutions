class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_freq = Counter(nums)
        nums_freq = sorted(nums_freq.items(), key = lambda x: x[1])

        freq_num = defaultdict(list)
        
        res = []
        for num, val in nums_freq:
            freq_num[val].extend([num] * val)

        for nums in freq_num.values():
            res.extend(sorted(nums, reverse = True))

        return res