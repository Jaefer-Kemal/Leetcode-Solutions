class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_count = Counter(nums)
        max_freq = max(num_count.values())

        buckets = [[] for _ in range(max_freq + 1)]

        for num, freq in num_count.items():
            buckets[freq].append(num)

        results = []

        for i in range(len(buckets) - 1, -1, -1):
            current = buckets[i]

            for num in current:
                results.append(num)

            if len(results) == k:
                return results