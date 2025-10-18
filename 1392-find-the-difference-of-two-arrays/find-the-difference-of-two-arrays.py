class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        distinct_nums1 = set(nums1)
        distinct_nums2 = set(nums2)
        diff_nums1 = distinct_nums1 - distinct_nums2
        diff_nums2 = distinct_nums2 - distinct_nums1

        return [list(diff_nums1), list(diff_nums2)]

        