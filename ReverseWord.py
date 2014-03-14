'''
@author: TNSTAR
'''
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        temp = s.split()
        temp = temp[::-1]
        return " ".join(temp)
sol = Solution()    
print sol.reverseWords("the sky is blue")