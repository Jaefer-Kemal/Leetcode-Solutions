class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        count_moves = 0

        for i in range(len(seats)):
            number_of_moves = abs(seats[i] - students[i])
            count_moves += number_of_moves
        
        return count_moves