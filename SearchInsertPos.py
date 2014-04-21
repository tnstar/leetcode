'''
Created on Apr 8, 2014

@author: C_TLU
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def bin_search(self, low, high, A, target):
        if low>high:
            if low == 0:
                return low
            else:
                return high
        mid = low+(high-low)/2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            self.bin_search(low,mid-1,A, target)
        else:
            self.bin_search(mid+1, high, A, target)
    def searchInsert(self, A, target):
        print self.bin_search(0,len(A)-1,A,target)
sol=Solution()

A = [1]
target = 0
print sol.searchInsert(A, target)
