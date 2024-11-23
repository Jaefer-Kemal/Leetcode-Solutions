class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        offset = 0

        ans = []
        dublicate_check = set()
        offset_check = set()
        while offset < len(nums):
            l = offset + 1
            r = len(nums) - 1

            if nums[offset] in offset_check:
                offset += 1
                continue
            else:
                offset_check.add(nums[offset])

            while l < len(nums) and r > offset and l<r:
                if nums[l] + nums[r] + nums[offset] == 0:
                    if not (frozenset([nums[l], nums[r], nums[offset]]) in dublicate_check):
                        dublicate_check.add(frozenset([nums[l], nums[r], nums[offset]]))
                        ans.append([nums[l], nums[r], nums[offset]])
                    l += 1
                    continue
                elif nums[l] + nums[r] + (nums[offset]) > 0:
                    r -= 1
                else:
                    l += 1

            offset += 1
        return ans


