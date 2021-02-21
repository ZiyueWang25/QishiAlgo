from typing import List


class Solution:

    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        target_col = grid[r0][c0]

        def check_avai(i,j):
            return  (i>=0 and i<len(grid) and j >= 0 and j < len(grid[0]))

        def dfs(i, j):
            if check_avai(i, j):
                    if grid[i][j] == target_col:
                        grid[i][j] = -1
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            dfs(i+dx, j+dy)
        def check(i,j):
            res = 0
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if check_avai(i+dx, j+dy) and grid[i+dx][j+dy] == -1:
                    res += 1
            return res == 4

        dfs(r0, c0)
        surrounded = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1 and check(i, j):
                    surrounded.append((i, j))
        for (i, j) in surrounded:
            grid[i][j] = target_col
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    grid[i][j] = color        
        return grid