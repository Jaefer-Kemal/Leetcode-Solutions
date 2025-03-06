
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = defaultdict(int)
        res = 0
        for num in answers:
            cnt[num] += 1

        for key, val in cnt.items():
            group = key + 1
            if key == 0:
                res += val

            elif val <= group:
                res += group
            else:
                res += (val + group - 1) // group * group
                
        return res