class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memo = set(nums)
        visited = set()
        maximum_seq = 0
        for num in memo:
            count = 1
            exist = num
            if exist not in visited:
                while exist + 1 in memo:
                    visited.add(exist)
                    count += 1
                    exist += 1

            maximum_seq = max(count, maximum_seq)
        
        return maximum_seq