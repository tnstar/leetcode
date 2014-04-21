'''
Created on Mar 18, 2014

@author: C_TLU
'''
import sys
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        peak = []
        if not prices:
            return 0
        prev = prices[0]
        peak.append(prev)
        if len(prices) == 1:
            return 0
        direction = 0 # direction -1 means down, 0  means flat, 1 means up
        for i in range(1,len(prices)):
            if prices[i] > prev:
                if direction == -1:
                    peak.append(prev)
                direction = 1
            elif prices[i] < prev:
                if direction == 1:
                    peak.append(prev)
                direction = -1
            else:
                pass #keep previous direction
            prev = prices[i]
        peak.append(prices[-1])
        #print peak
        min_val = max_val = peak[0]
        max_profit = 0
        for i in range(1,len(peak)):
            print max_profit
            #print peak[i]
            if peak[i]>peak[i-1]:
                if (peak[i]-peak[i-1]) > max_profit:
                    max_profit = peak[i]-peak[i-1]
                if peak[i]>max_val:
                    max_val = peak[i]
                if (peak[i] - min_val) > max_profit:
                    max_profit = peak[i] - min_val
            else:
                if peak[i]<min_val:
                    min_val = peak[i]
        return max_profit

sol = Solution()
print sol.maxProfit([3,3,5,0,0,3,1,4])