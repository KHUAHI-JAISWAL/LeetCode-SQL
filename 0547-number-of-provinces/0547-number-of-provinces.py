class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # Brute Force: Har city ke liye connected cities ko repeatedly check karke visited mark karo — Time: O(Nsequere),Space: O(N).

        #Best Approach: DFS use karke har unvisited city se traversal start karo; har DFS ek province count karta hai — Time: O(N sequer),Space: O(N)


        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)

            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces += 1

        return provinces





        