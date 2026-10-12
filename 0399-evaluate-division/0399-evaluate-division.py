class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:


        #Brute Force: Har query ke liye DFS se source variable se destination tak path search karo aur edge ratios multiply karo — Time: O(Q(V+E)), Space: O(V+E).
        #Best Approach: Weighted graph + DFS; har equation ko ratio ke saath store karo aur har query ke liye connected path ka product calculate karo — Time: O(Q(V+E)), Space: O(V+E).





        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0

            if src == dst:
                return 1.0

            visited.add(src)

            for neighbor, weight in graph[src]:
                if neighbor not in visited:
                    result = dfs(neighbor, dst, visited)
                    if result != -1.0:
                        return weight * result

            return -1.0

        return [
            dfs(a, b, set())
            for a, b in queries
        ]
        