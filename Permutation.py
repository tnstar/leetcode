class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def myfunc(self,num,index):
        if index == len(num):
            print num
            return
        for i in range(index,len(num)):
            num[index],num[i] = num[i],num[index]
            self.myfunc(num,index+1)
            num[index],num[i] = num[i],num[index]
            
    def permute(self, num):
        self.myfunc(num, 0)
        
sol = Solution()
sol.permute([5,8,1,6])