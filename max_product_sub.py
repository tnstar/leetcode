

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        max_val = A[0]
        min_val = A[0]
        ans = A[0]
        for i in range(1,len(A)):
            a = max_val*A[i]
            b = min_val*A[i]
            max_val = max(a,b,A[i])
            min_val = min(a,b,A[i])
            ans = max(ans,max_val)
        return ans

sol = Solution()
print sol.maxProduct([1,-2,3])