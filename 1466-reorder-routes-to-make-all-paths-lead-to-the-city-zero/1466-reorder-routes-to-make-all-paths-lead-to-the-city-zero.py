class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:


        #Brute Force: Har city se city 0 tak path check karke wrong-direction roads reverse karo — Time: O(N2 squere) ,Space: O(N).
        #Best Approach: DFS from city 0; har road jo DFS traversal mein 0 se door jaane wali original direction mein mile, use reverse karna hoga — Time: O(N), Space: O(N).


        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = set()
        changes = 0

        def dfs(city):
            nonlocal changes
            visited.add(city)

            for neighbor, cost in graph[city]:
                if neighbor not in visited:
                    changes += cost
                    dfs(neighbor)

        dfs(0)
        return changes
