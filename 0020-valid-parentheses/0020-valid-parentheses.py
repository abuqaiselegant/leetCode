class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")":"(","}":"{","]":"["
        }

        for c in s:
            if c in closeToOpen.values():
                stack.append(c)
            elif c in closeToOpen:
                if not stack or stack[-1]!=closeToOpen[c]:
                    return False
                stack.pop()
        return not stack
            

        