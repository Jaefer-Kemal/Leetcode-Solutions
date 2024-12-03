class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        sorted_cnt = sorted(cnt.items(),key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(sorted_cnt[i][0])
        return res








        # c = Counter(nums)
        
        # c = dict(sorted(c.items(),reverse = True, key = lambda a:a[1]))
        # res = []
        # for key in c.keys():
        #     if k!=0:
        #         res.append(key)
        #     else:
        #         break
        #     k-=1
        # return res
        