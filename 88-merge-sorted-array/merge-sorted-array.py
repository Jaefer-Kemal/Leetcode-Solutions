from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1  # Last element of nums1's valid section
        j = n - 1  # Last element of nums2
        k = m + n - 1  # Last position of nums1
        
        # Merge from the back to avoid overwriting nums1's initial elements
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If nums2 still has elements left, add them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
