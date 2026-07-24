class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens :
            if token not in "+-/*":
                stack.append(token)
            else :
                right = int(stack.pop())
                left = int(stack.pop())
                match token:
                    case "+" : res = right + left
                    case "-" :res =left-right
                    case "*" : res =right*left
                    case "/"  :res= left/right

                stack.append(res)

        return int(stack[-1])