from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        n = len(board)
        m = len(board[0])

        def helper(i, j):
            nonlocal board
            if 0 <= i < n and 0 <= j < m:
                if board[i][j] in ["X", "E"]:
                    return
                if board[i][j] == "O":
                    board[i][j] = "E"
                    helper(i - 1, j)
                    helper(i + 1, j)
                    helper(i, j - 1)
                    helper(i, j + 1)
            return

        for i in range(n):
            helper(i, 0)
            helper(i, m - 1)
        for j in range(m):
            helper(0, j)
            helper(n - 1, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "E":
                    board[i][j] = "O"
