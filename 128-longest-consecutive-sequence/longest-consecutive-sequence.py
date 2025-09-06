class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memo = set(nums)
        visited = set()
        maximum_seq = 0
        for num in memo:
            count = 1
            curr = num
            if curr not in visited:
                while curr + 1 in memo:
                    visited.add(curr)
                    count += 1
                    curr += 1

            maximum_seq = max(count, maximum_seq)
        
        return maximum_seq