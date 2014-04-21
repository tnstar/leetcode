class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        lists = []
        for i in range(1,numRows+1):
            sublist = []
            lists.append(sublist)
            for j in range(i):
                if j == 0 or j==i-1:
                    sublist.append(1)
                else:
                    sublist.append(lists[i-2][j-1]+lists[i-2][j])
        return lists
sol = Solution()
print sol.generate(4)