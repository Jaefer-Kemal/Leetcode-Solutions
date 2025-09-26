class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_nums1 = set(nums1)
        unique_nums2 = set(nums2)
        answer1 = 0
        answer2 = 0

        for num in nums1:
            if num in unique_nums2:
                answer1 += 1
                

        for num in nums2:
            if num in unique_nums1:
                answer2 += 1
                
        
        return [answer1, answer2]
        