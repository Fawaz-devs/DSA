class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
  

        if len(s) != len(t) :
            return False

        list =  set(s)

        for item in s :
            if s.count(item) != t.count(item) :
                return False

        return True