class Solution:
    def longestPalindrome(self, s):
        result = ''

        # each index repeat
        for i in range(len(s)):
            # case. odd length string (i.e. "babad")
            temp = self.window(s, i, i)
            # if the other index has a palindromic substring, rewrite result
            if len(result) < len(temp): 
                result = temp
            # case. even length string (i.e. "abbd")
            temp = self.window(s, i, i+1)
            # if the other index has a palindromic substring, rewrite result
            if len(result) < len(temp):
                result = temp
        return result

    # start, end are the middle indexes from inner to outer
    def window(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return  s[start+1:end]