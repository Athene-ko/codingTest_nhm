# Sol1. list & index
class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ['[', '(', '{']
        closeBrackets = [']', ')', '}']
        stack = []
        
        for i in s:
            if i in openBrackets:
                stack.append(i)
            elif len(stack) != 0 and stack[-1] == openBrackets[closeBrackets.index(i)]:
                    stack.pop()
            else:
                return False
        return len(stack) == 0

# Sol2. dict & pop
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")", "{":"}", "[":"]"}
        stack = []
        
        for i in s:
            if i in brackets:
                stack.append(i)
            elif len(stack) == 0 or brackets[stack.pop()] != i:
                return False
        print(f'stack: {stack}')
        return len(stack) == 0
        
        