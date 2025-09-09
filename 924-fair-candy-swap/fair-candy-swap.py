class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        total_alice = sum(aliceSizes)
        total_bob = sum(bobSizes)
        mid = (total_alice - total_bob) // 2

        unique_alice = set(aliceSizes)
        unique_bob = set(bobSizes)

        for can in aliceSizes:
            if can - mid in unique_bob:
                return [can, can - mid]
        