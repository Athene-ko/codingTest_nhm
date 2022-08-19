class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
         
        if numRows == 1 or len(s) <= numRows:
            return s
        
        result = [''] * numRows
        idx, step = 0, 1
        
        for i in s:
            result[idx] += i
            if idx == 0:
                step = 1
            elif idx == numRows -1:
                step = -1
            idx += step

        return ''.join(result)