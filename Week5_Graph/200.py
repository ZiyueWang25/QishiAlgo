from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        def helper(i, j):
            nonlocal grid
            if 0 <= i <= m -1 and 0 <= j <= n - 1:
                if grid[i][j] == "1":
                    grid[i][j] = "2"
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        helper(i+dx, j+dy)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    helper(i, j)
        return res