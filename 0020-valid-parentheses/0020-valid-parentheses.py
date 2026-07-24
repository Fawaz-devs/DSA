class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
                        ")": "(",
                        "}": "{",
                        "]": "["
                    }
        res = []
        for c in s :
            if c in "({[":
                res.append(c)
            else :
                if len(res) == 0 :
                    return False
                elif res[-1] == brackets[c] :
                    res.pop(-1)
                else :
                    return False
        if len(res) == 0:
            return True
        return False
                    

            
                
        
                