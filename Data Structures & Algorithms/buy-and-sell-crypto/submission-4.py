class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0 
        l = 0
        h = 1
        while h < len(prices):
            best = max(prices[h]- prices[l], best)
            if(prices[l] > prices[h]):
                l=h
            else:
                h+=1
        return best