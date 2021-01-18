# A casino offers a card game with 26 red and 26 black cards. The cards are shuffled and the dealer draws cards
# one by one (without putting back). You can ask the dealer to stop at any time you like. Upon stopping, you win $1
# for each red card drawn, and lose \$1 for each black card. What is the optimal stopping policy to maximize expected
# payoff and how much you are willing to pay for this game?
#
# Hint: Let the system state be (b,r): the number of black and red cards still left in the deck. The (conditional)
# action space is really just {continue, stop} (at b, r).
# - What's the expected payoff E[f(b,r)]?


def dcg(b, r):
    dp = [[0] * 27 for _ in range(27)]
    for r in range(27):
        dp[0][r] = 0
    for b in range(27):
        dp[b][0] = b
    for b in range(1,27):
        for r in range(1,27):
            dp[b][r] = max(b-r, 0, dp[b - 1][r] * b / (b + r) + dp[b][r - 1] * r / (b + r))
    return dp[b][r]


if __name__ == '__main__':
    print(dcg(26,26))