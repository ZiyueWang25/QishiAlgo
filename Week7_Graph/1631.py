import heapq
from typing import List


class Solution:

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        visited = set([])
        q = [(0, 0, 0)]
        while q:
            curr, x, y = heapq.heappop(q)
            if (x, y) == (n-1, m-1):
                return curr
            visited.add((x, y))
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_x = x+dx
                new_y = y+dy
                if 0 <= new_x < n and 0 <= new_y < m and (new_x, new_y) not in visited:
                    next_h = heights[new_x][new_y]
                    next_val = max(abs(next_h-heights[x][y]), curr)
                    heapq.heappush(q, (next_val, new_x, new_y))