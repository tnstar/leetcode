class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    part_res = {}
    def pow(self,x,n):
        if n>=0:
            return self.help_pow(x, n)
        else:
            return 1/float(self.help_pow(x, -n))
    def help_pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if not self.part_res.has_key(n/2):
            self.part_res[n/2] = self.help_pow(x, n/2)
        if not self.part_res.has_key(n-n/2):
            self.part_res[n-n/2] = self.help_pow(x,n - n/2)
        return self.part_res[n/2]*self.part_res[n - n/2]

sol = Solution()
print sol.pow(34.00515,-3)
print 34.00515**(-3)