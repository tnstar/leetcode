class Solution:
    # @return a string
    def countAndSay(self, n):
        n = n-1
        if n == 0:
            return "1"
        num_arr = "1"
        for i in range(n):
            cur_num = num_arr[0]
            num_count = 0
            next_num_arr = ""
            arr_len = len(num_arr)
            for j in range(arr_len):
                if cur_num == num_arr[j]:
                    num_count +=1
                else:
                    next_num_arr = next_num_arr+str(num_count)+cur_num
                    cur_num = num_arr[j]
                    num_count = 1
            next_num_arr = next_num_arr+str(num_count)+cur_num
            num_arr = next_num_arr
            next_num_arr = ""
            num_count = 0
        return num_arr

sol=Solution()
print sol.countAndSay(6)
                    