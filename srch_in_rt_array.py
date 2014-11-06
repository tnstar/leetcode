class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    
    #test case
    # 6 7 1 2 3 4 5
    # 2 3 4 5 6 7 1
    def search(self, A, target):
        lp = 0
        rp = len(A)-1
        while lp<=rp:
            mid = (lp+rp)/2 # need to take care of over flow in C
            if A[mid] == target:
                return mid
            if A[mid] >= A[lp]:
                if target < A[mid] and target >= A[lp]:
                    rp = mid -1
                else:
                    lp = mid +1
            else:
                if target > A[mid] and target <= A[rp]:
                    lp = mid +1
                else:
                    rp = mid -1
        return -1

sol = Solution()
print sol.search([6,7,1,2,3,4,5], 5)
            