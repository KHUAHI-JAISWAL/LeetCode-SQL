class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        #Brute Force: Har minute grid scan karke fresh oranges ko rotten karo — Time: O((mn)²), Space: O(1) auxiliary space.
        #Best (Multi-source BFS): Saare rotten oranges ko queue mein daalkar level-by-level fresh oranges rot karo — Time: O(mn), Space: O(mn).

        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        minutes = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and 0 <= nc < n
                            and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1

        