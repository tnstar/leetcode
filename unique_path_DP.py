class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[0][0] = 0
        