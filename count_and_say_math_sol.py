class Solution:
    # @return a string
    def countAndSay(self, n):
        if int(n)<0:
            return
        elif int(n) == 0:
            return 1
        else:
            n = self.countAndSay(n-1)
            n = int(n)
            num_len = len(str(n))
            cur_offset = num_len -1
            AssertionError(cur_offset>0)
            cur_num = n/(10**cur_offset)
            cur_num_count = 0
            next_n = 0
            for i in range(num_len):
                cur_offset = num_len-i-1
                if cur_num == n/(10**cur_offset):
                    cur_num_count +=1
                else:
                    next_n=(next_n*100)+(cur_num_count*10)+cur_num
                    cur_num = n/(10**cur_offset)
                    cur_num_count = 1
                n = n - cur_num*10**cur_offset
                #print cur_num,cur_num_count,n
            #adding the missing match for the last one
            next_n = (next_n*100)+(cur_num_count*10)+cur_num
            AssertionError(next_n>0)
            return str(next_n)

sol = Solution()
print sol.countAndSay(10)