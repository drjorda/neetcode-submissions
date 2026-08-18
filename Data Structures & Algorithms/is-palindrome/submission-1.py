class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s) - 1
        i = 0
        while(True):
            while(i < len(s) and s[i].isalnum() == False):
                i +=1
            while(j < len(s) and j > 0 and s[j].isalnum() == False):
                j-=1
            if(j <= i ):
                return True
            if(s[i].lower() != s[j].lower()):
                return False
            j-=1
            i+=1