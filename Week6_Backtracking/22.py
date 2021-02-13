class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def back(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                back(S+'(', left+1, right)
            if right < left:
                back(S+')', left, right+1)
        back()
        return ans