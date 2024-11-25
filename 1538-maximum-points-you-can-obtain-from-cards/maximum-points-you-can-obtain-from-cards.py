class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pre_l = [cardPoints[0]]
        pre_r = [cardPoints[-1]]
        maxim = 0
        for r in range(1,k):
            pre_l.append(pre_l[r - 1] + cardPoints[r])
            pre_r.append(pre_r[r-1] + cardPoints[-(r + 1)])
        print(pre_l)
        print(pre_r)
        
        maxim = max(pre_l[k - 1], pre_r[k - 1])

        for i in range(0,k-1):
            sum_ = pre_l[i] + pre_r[-(i+2)]
            maxim = max(maxim, sum_)
            sum_ = 0
        return maxim


        