class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        #Brute Force: Har room ko repeatedly check karo aur reachable rooms mark karo jab tak koi naya room na mile — Time: O(N+K), Space: O(N).
        #Best Approach: DFS se room 0 se start karo aur keys use karke saare reachable rooms visit karo — Time: O(N+K), Space: O(N).


        visited = set()

        def dfs(room):
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)
        return len(visited) == len(rooms)
        