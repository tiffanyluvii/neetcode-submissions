class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False


        # for char in s:
        #     if (char == '[' or char == '(' or char == '{'):
        #         stack.append(char)
        #     elif (stack == []):
        #         return False;
        #     elif(char == ']' and stack[-1] == '['):
        #         stack.pop()
        #     elif(char == ')' and stack[-1] == '('):
        #         stack.pop()
        #     elif(char == '}' and stack[-1] == '{'):
        #         stack.pop()
        #     else:
        #         return False
        # if (stack == []):
        #     return True
        # return False



        