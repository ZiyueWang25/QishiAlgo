# We want to use k eggs to find out the highest floor from which an egg will not break when dropped from that floor.
# If an egg is dropped and does not break, it can be dropped again. An interesting thing to consider is a
# minimax problem: The best (mini) number of drops in the worst case (max) scenario to determine the "breakeven" floor.
# Find that number.

# Hint: What's the minimax value if we only have 1 egg? For the other extreme, infinite number of eggs?
# How about 2 (=1+1) eggs? 3 (=2+1) eggs?
import math


class Solution:

    def superEggDrop(self, K, N):
        dp = [[0] * (K + 1) for i in range(N + 1)]
        # dp[M][K]means that, given K eggs and M moves,
        # what is the maximum number of floor that we can check.
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N: return m

    def superEggDrop(self, K, N):
        # 1 dimensional version
        dp = [0, 0]
        m = 0
        while dp[-1] < N:
            for i in range(len(dp) - 1, 0, - 1):
                dp[i] += dp[i - 1] + 1
            if len(dp) < K + 1:
                dp.append(dp[-1])
            m += 1
        return m