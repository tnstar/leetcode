class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        lenA = len(A)
        p_end = lenA - 1
        p_start = 0
        
        while p_start <= p_end:
            if A[p_start] == elem:
                A[p_start] = A[p_end]
                p_end = p_end - 1
            else:
                p_start = p_start + 1
        print A,p_end
A = [1,2,3,4,5,5,5,6]

sol = Solution()
sol.removeElement(A, 5)
            