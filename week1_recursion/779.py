class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1 or K == 1:
            return 0
        else:
            if K % 2 == 1:
                return int(self.kthGrammar(N-1, (K+1)//2) == 1)
            else:
                return int(self.kthGrammar(N-1, K//2) == 0)