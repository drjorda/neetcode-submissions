from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictMap = {}
        result = []
        j=len(nums) -1
        for i, n in enumerate(nums):
            goal = target - n
            if goal in dictMap:
                return [dictMap.get(goal), i]
            dictMap[n] = i
