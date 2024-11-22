class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = 0
        r = 0
        
        merged_array = []
        
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                merged_array.append(nums1[l])
                l += 1
            else:
                merged_array.append(nums2[r])
                r += 1
            
        merged_array += (nums1[l:] + nums2[r:])
        
        n = len(merged_array)
        if n % 2 == 0:
            median = (merged_array[n//2] + merged_array[n//2 - 1]) / 2
        else:
            median = merged_array[n//2]
            
        return median
            