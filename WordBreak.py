class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True]
        for i in xrange(1,len(s)+1):
            dp += [any(dp[j] and s[j:i] in wordDict for j in xrange(i))]
        return dp[-1]
