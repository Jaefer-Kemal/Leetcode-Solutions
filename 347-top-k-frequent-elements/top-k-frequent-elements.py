class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = dict(sorted(c.items(),reverse = True, key = lambda a:a[1]))
        res = []
        for key in c.keys():
            if k!=0:
                res.append(key)
            else:
                break
            k-=1
        return res
        