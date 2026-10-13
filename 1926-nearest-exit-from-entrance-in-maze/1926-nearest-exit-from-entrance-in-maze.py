class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:

        #Brute Force: Har possible path ko explore karke nearest exit find karo — Time: O(4mn), Space: O(mn) (DFS recursion; simple path enumeration).

        #Best Approach (BFS): Queue se level-by-level cells explore karo aur pehla boundary exit return karo — Time: O(mn), Space: O(mn).


        m, n = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, steps = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                        return steps + 1

                    maze[nr][nc] = '+'
                    q.append((nr, nc, steps + 1))

        return -1

        