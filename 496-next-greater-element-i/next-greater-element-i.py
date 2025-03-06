class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = defaultdict(lambda : -1)

        for num in nums2:
            
            while stack and stack[-1] < num:
                val = stack.pop()
                next_greater[val] = num
            
            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(next_greater[num])
            
        return ans
        