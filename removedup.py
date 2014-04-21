'''
Created on Apr 19, 2014

@author: C_TLU
'''
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return 1
        p_front = 0
        p_end =1
        A_len = len(A)
        while p_end<A_len:
            if A[p_front] == A[p_end]:
                p_end += 1
            else:
                p_front+=1
                A[p_front] = A[p_end]
                p_end += 1
        A = A[:p_front+1]
        return p_front+1
        
sol = Solution()
print sol.removeDuplicates([1,1]) 