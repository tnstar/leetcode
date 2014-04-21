'''
Created on Apr 19, 2014

@author: C_TLU
'''
#===============================================================================
# bit manipulation problem
# need an array to store the bit
# if the bit appear once we store it
#===============================================================================
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        bit_arr = [0 for i in range(32)]
        for num in A:
            for i in range(32):
                bit_arr[i] += (num&(~0&(1<<i)))>>i
                if bit_arr[i] == 3:
                    bit_arr[i] = 0
        # recover from bit_arr
        result = 0
        str1 = "0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1"
        str1 = "".join(reversed(str1.split(", ")))
        print str1
        print int(str1,2)
        #=======================================================================
        # for i in range(32):
        #     result = int(result|(bit_arr[i]<<i))
        #     print result,type(result)
        #=======================================================================
        #print result

sol = Solution()
sol.singleNumber([1,1,1,-2])
print type(-2147483648)