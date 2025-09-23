class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        good_pair = 0

        for num in nums:
            good_pair += count[num]
            count[num] += 1
        
        return good_pair
        