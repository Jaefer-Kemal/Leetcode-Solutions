class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono_decreasing_stack = []
        next_greater = defaultdict(lambda : -1)

        for num in nums2:
            while mono_decreasing_stack and mono_decreasing_stack[-1] < num:
                val = mono_decreasing_stack.pop()
                next_greater[val] = num
            
            mono_decreasing_stack.append(num)

        ans = []
        for num in nums1:
            ans.append(next_greater[num])
            
        return ans
        