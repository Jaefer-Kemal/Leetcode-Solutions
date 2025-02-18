class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        cnt[0] = -1

        maximum_substring = 0

        r = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count += -1
            else:
                count += 1
            
            if count in cnt:
                maximum_substring = max(maximum_substring,r - cnt[count])
            else:
                cnt[count] = r
            
        return maximum_substring

                


        