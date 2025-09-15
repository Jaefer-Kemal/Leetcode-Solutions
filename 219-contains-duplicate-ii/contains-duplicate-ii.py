class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate_check = defaultdict(int)

        for i, num in enumerate(nums):
            if num not in duplicate_check:
                duplicate_check[num] = i
            else:
                if i - duplicate_check[num] <= k:
                    return True
                duplicate_check[num] = i
        
        return False