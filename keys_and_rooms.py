from types import List

# 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        
        q = [] + rooms[0]
        
        while q:
            r = q.pop() # next room key
            if r not in visited:
                q = q + rooms[r]
                visited.add(r)
        
        return len(rooms) == len(list(visited))