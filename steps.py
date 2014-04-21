'''
Created on Apr 15, 2014

@author: C_TLU
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        dp = [0 for i in range(n+1)]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            dp[0] = 1
            dp[1] = 1
            for i in range(2,n+1):
                dp[i] = dp[i-1]+dp[i-2]
            return dp[n]

sol = Solution()
print sol.climbStairs(2)