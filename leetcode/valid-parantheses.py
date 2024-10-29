class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        stack = []
        
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif stack:
                inner_parantheses = stack.pop()
                if char == ")" and inner_parantheses != "(":
                    return False
                elif char == "}" and inner_parantheses != "{":
                    return False
                elif char == "]" and inner_parantheses != "[":
                    return False
            else: 
                return False
                    
        if len(stack) == 0:
            return True
        return False
