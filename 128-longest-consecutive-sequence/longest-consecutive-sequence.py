class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        s = set(nums)
        cnt = 0
        longest = 1
        seen = {}
        for r in range(len(nums)):
            if nums[r] - 1 not in s:
                num = nums[r]
                while num in s:
                    if num in seen:
                        cnt += seen[num]
                        break
                    
                    cnt += 1
                    seen[num] = cnt
                    num += 1
                    
                longest = max(longest, cnt)
            cnt = 0

        return longest
