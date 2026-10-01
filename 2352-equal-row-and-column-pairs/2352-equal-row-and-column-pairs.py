class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:

        row_count = {}

        for row in grid:
            row = tuple(row)
            row_count[row] = row_count.get(row, 0) + 1

        ans = 0

        for j in range(len(grid)):
            col = []

            for i in range(len(grid)):
                col.append(grid[i][j])

            col = tuple(col)

            if col in row_count:
                ans += row_count[col]

        return ans




       #Brute Force: Har row ko har column se element-by-element compare karo → Time: O(n³), Space: O(1)
       #best: Rows ki frequency HashMap mein store karke har column ko tuple bana kar lookup karo → Time: O(n²), Space: O(n²)

       