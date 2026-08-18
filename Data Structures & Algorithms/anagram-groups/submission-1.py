from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictMap = defaultdict(list)
        result = []
        for item in strs:

            dictMap[tuple(sorted(item))].append(item)
        for anagram in dictMap:
            result.append(dictMap[anagram])
        return result