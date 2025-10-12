class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        num_counts_1 = Counter(nums1)
        num_counts_2 = Counter(nums2)

        for num in num_counts_1:
            for _ in range(min(num_counts_1[num], num_counts_2[num])):
                res.append(num)
        
        return res
        
        