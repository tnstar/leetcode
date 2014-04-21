'''
Created on Apr 21, 2014

@author: C_TLU
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        #populating hashtable
        rec = {}
        for i in num:
            rec[i] = True
        max_len = 0
        low_index = 0
        upper_index = 0
        for i in num:
            if rec.has_key(i):
                upper = 0
                uindex = i+1
                while rec.has_key(uindex):
                    del rec[uindex]
                    upper +=1
                    uindex +=1
                lower = 0
                lindex = i-1
                while rec.has_key(lindex):
                    del rec[lindex]
                    lower +=1
                    lindex -=1
            uindex -=1
            lindex +=1
            seq_len = uindex-lindex+1
            if seq_len>max_len:
                max_len = seq_len
                low_index = lindex
                upper_index = uindex
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print sol.longestConsecutive([1,2,3,3,1,4])