class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        i = 0
        min_shots = 0

        # Checking in ascending order 
        shots_1 = 0
        while i < len(points):
            x1 = points[i][0]
            x2 = points[i][1]

            while i < len(points) and (points[i][0] <= x1 <= points[i][1] or  points[i][0] <= x2 <= points[i][1]):
                i += 1


            shots_1 += 1

        i = len(points) - 1
        
        # Checking in descending order
        shots_2 = 0
        while i >= 0:
            x1 = points[i][0]
            x2 = points[i][1]

            while i >= 0 and (points[i][0] <= x1 <= points[i][1] or  points[i][0] <= x2 <= points[i][1]):
                i -= 1

            shots_2 += 1
        
        min_shots = min(shots_2, shots_1)

        return min_shots