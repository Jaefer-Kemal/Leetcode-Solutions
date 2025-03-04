class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        i = 0
        min_shots = 0
        print(points)
        
        while i < len(points):
            x1 = points[i][0]
            x2 = points[i][1]

            while i < len(points) and (points[i][0] <= x1 <= points[i][1] or  points[i][0] <= x2 <= points[i][1]):
                i += 1


            min_shots += 1

        i = len(points) - 1

        shots = 0
        while i >= 0:
            x1 = points[i][0]
            x2 = points[i][1]

            while i >= 0 and (points[i][0] <= x1 <= points[i][1] or  points[i][0] <= x2 <= points[i][1]):
                i -= 1

            shots += 1
        
        min_shots = min(min_shots, shots)

        return min_shots
