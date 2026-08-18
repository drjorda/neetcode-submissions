from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictMap = {}
        result = []
        j=len(nums) -1
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in dictMap:
                return [dictMap.get(goal), i]
            dictMap[nums[i]] = i
