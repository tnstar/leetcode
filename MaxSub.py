'''
Created on Apr 15, 2014

@author: C_TLU
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        dp = [0 for i in range(len(A)+1)]
        dp[0] = 0
        if not A:
            return dp[0]
        for i in range(1,len(A)+1):
            dp[i] = max(dp[i-1]+A[i-1],A[i-1])
        return max(dp)
    
A = [-1,-2,3]
sol = Solution()
print sol.maxSubArray(A)