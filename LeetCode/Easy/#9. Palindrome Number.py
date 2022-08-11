class Solution:
    def isPalindrome1(self, x: int) -> bool:
        # Solution 1. Convert int to string
        stringX = str(x)
        reverse = ''
        
        for i in stringX[::-1]:
            reverse += i
        if reverse == stringX:
            return True
        else:
            return False

    def isPalindrome2(self, x: int) -> bool:
        # Solution 2. without converting int to string
        inputX = x
        reverse = 0
        
        if x < 0:
            return False
        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10
        if reverse == inputX:
            return True
        return False
    
        
        