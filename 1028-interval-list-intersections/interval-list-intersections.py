class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []

        # p1 pointer for the firstList
        p1 = 0
        # p2 pointer for the secondList
        p2 = 0
        results = []

        while p1 < len(firstList) and p2 < len(secondList):
            start = max(firstList[p1][0], secondList[p2][0])
            end = min(firstList[p1][1], secondList[p2][1])

            if start <= end:
                results.append([start,end])
        
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1

            
        return results