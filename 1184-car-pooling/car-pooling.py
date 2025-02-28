class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        intervals = [0] * 1001

        for trip in trips:
            start = trip[1]
            end = trip[2]
            intervals[start] += trip[0]
            intervals[end] -= trip[0]
        

        for i in range(1,len(intervals)):
            if intervals[i - 1] > capacity:
                return False
            intervals[i] += intervals[i - 1]

        return True