class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        newRomanInt = 0
        
        newRomanStr = s
        newRomanStr = newRomanStr.replace("IV","IIII").replace("IX","VIIII")
        newRomanStr = newRomanStr.replace("XL","XXXX").replace("XC","LXXXX")
        newRomanStr = newRomanStr.replace("CD","CCCC").replace("CM","DCCCC")
        
        for i in newRomanStr:
            newRomanInt += int(romanNumerals[i])
        return newRomanInt