class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        len_arr = len(A)
        if len_arr<3:
            return len_arr
        same_ind = False
        index_x = 0
        index_y = 1
        while True:
            if index_x >= len_arr or index_y >= len_arr:
                break
            if A[index_x] == A[index_y]:
                if same_ind == False:
                    same_ind = True
                else:
                    del A[index_y] # it doesn't matter which one
                    len_arr = len_arr -1
                    continue
            else:
                same_ind = False
            index_x = index_x+2;
            index_x,index_y = index_y,index_x
        return A
sol = Solution()
print sol.removeDuplicates([1,1,2,2,2,2,2,3,3,3,4])