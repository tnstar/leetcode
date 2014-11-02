class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        else:
            str_len = len(s)
            start = 0
            count = 0
            for i in range(str_len):
                if s[str_len-i-1] == ' ':
                    if start == 0:
                        start = 1
                    elif start == 2:
                        break
                else:
                    start = 2
                    count=count+1
            return count