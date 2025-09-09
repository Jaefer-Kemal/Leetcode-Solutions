class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = defaultdict(int)

        for num in nums:
            if num in candidates:
                candidates[num] += 1

            elif len(candidates) < 2:
                candidates[num] += 1
            
            else:
                erase = []
                for candidate in candidates.keys():
                    candidates[candidate] -= 1
                    if candidates[candidate] == 0:
                        erase.append(candidate)
                        
                for e in erase:
                    del candidates[e]


        counts = defaultdict(int)
        for num in nums:
            if num in candidates:
                counts[num] += 1

        res = []
        for candidate, freq in counts.items():
            if freq > len(nums) // 3:
                res.append(candidate)
        
        return res

