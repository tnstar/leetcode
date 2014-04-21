'''
Created on Mar 31, 2014

@author: c_tlu
'''
class Solution:
    # @return an integer
    def numTrees(self, n):
        arr = [0 for i in range(n+1)]
        arr[0] = 1
        arr[1] = 1
        for i in range(2,n+1):
            for j in range(0,i):
                arr[i] = arr[i] + arr[0+j]*arr[i-j-1]
        return arr[n]
    
sol = Solution()
print sol.numTrees(4)