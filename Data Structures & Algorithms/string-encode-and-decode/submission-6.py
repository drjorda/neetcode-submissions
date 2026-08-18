class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result=result + s + "#1" 
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        j = 0
        for i in range(len(s)):
            if(i != len(s)-1):
                if(s[i] + s[i+1] == "#1"):
                    result.append(s[j:i])
                    j = i+2
        return result

