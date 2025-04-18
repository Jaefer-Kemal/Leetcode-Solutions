class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        open_rooms = [0] * len(rooms)
        open_rooms[0] = 1

        queue = deque(rooms[0])

        while queue:
            key = queue.popleft()

            if open_rooms[key] == 0:
                for k in rooms[key]:
                    if open_rooms[k] == 0:
                        queue.append(k)
                
                open_rooms[key] = 1
            

        for room in open_rooms:
            if room == 0:
                return False
        
        return True