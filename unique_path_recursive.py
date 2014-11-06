# permutation

class Solution:
    # @return an integer
    dp = [[-1 for i in range(101)] for j in range(101)]
    dp[0][0] = 0
    def Helper(self,m,n):
        if m == 0:
            return 1
        elif n == 0:
            return 1
        else:
            if self.dp[m-1][n] == -1:
                self.dp[m-1][n] = self.Helper(m-1,n)
            if self.dp[m][n-1] == -1:
                self.dp[m][n-1] = self.Helper(m,n-1)
            return self.dp[m-1][n]+self.dp[m][n-1]
    def uniquePaths(self, m, n):
        self.dp = [[-1 for i in range(101)] for j in range(101)]
        return self.Helper(m-1, n-1)


sol=Solution()
print sol.uniquePaths(1,2)