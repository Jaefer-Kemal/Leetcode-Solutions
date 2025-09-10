class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subarr_zero = []
        count = 0
        occurence = 0
        memo = {}
        for num in nums:
            if num == 0:
                count += 1
            else:
                subarr_zero.append(count)
                count = 0
        
        subarr_zero.append(count)
        print(subarr_zero)
        for num in subarr_zero:
            if num in memo:
                occurence += memo[num]
                continue

            if num != 0:
                cnt = 0
                for n in range(1,num + 1):
                    cnt += n
                    memo[n] = cnt
                    
                occurence += cnt
        return occurence