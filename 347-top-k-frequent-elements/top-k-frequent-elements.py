class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_freq = Counter(nums)
        count_freq = dict(sorted(count_freq.items(), key=lambda x:x[1], reverse=True))
        res = []
        for num, freq in count_freq.items():
            if len(res) < k:
                res.append(num)
            else:
                break

        return res