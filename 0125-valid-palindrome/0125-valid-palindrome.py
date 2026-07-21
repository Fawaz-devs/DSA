class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ""
        for c in s : 
            if c.isalnum() :
                strs+= c.lower()

        start = 0
        end = len(strs) - 1
        for ch in strs :
            if strs[start]!=strs[end]:
                return False
            else : 
                start += 1
                end -= 1

        return True

