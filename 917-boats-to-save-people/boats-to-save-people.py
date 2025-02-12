class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()


        front = 0
        back = len(people) - 1

        minimum_boats = 0

        while front <= back:
            if people[front] + people[back] <= limit:
                front += 1
                back -= 1
            else:
                back -= 1

            minimum_boats += 1

        
        return minimum_boats
        