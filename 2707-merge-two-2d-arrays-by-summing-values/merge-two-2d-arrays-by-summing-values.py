class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dict_nums1 = dict(nums1)
        dict_nums2 = dict(nums2)
        unique_id = sorted(set(list(dict_nums1.keys()) + list(dict_nums2.keys())))
        res = []

        for id_ in unique_id:
            val = dict_nums1.get(id_, 0) + dict_nums2.get(id_, 0)
            res.append([id_, val])
        
        return res
        