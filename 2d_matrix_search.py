class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        else:
            self.m=len(matrix)
            self.n=len(matrix[0])
            self.matrix_len = self.m*self.n
            self.tgt = target
            lp = 0
            rp = self.matrix_len - 1
            while lp<=rp:
                mid = (lp+rp)/2
                if matrix[mid/self.n][mid%self.n]>self.tgt:
                    rp = mid - 1
                elif matrix[mid/self.n][mid%self.n]<self.tgt:
                    lp = mid +1
                else:
                    return True
            return False
sol = Solution()
print sol.searchMatrix([[1,2],[3,4]], 4)