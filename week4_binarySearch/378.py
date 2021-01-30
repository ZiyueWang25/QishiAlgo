import heapq

class Solution:
    def kthSmallest(self, matrix, k) -> int:
        n = len(matrix)
        minHeap = []
        for r in range(min(k, n)):
            heapq.heappush(minHeap, (matrix[r][0], r, 0))

        while k:
            element, r, c = heapq.heappop(minHeap)
            if c < n - 1:
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))
            k -= 1
        return element