class Solution:

    def hIndex(self, citations: List[int]) -> int:
        total_paper = len(citations)
        low = 0
        high = total_paper - 1
        res = 0

        while low <= high:
            mid = (low + high) // 2
            h = total_paper - mid

            if citations[mid] >= h:
                res = h
                high = mid - 1

            else:
                low = mid + 1
        
        return res 