class Solution:
    def countAndSay(self, n: int) -> str:
      # countAndSay(1) = 1
      if n == 1:
        return "1"
      
      # 재귀 활용
      recur = self.countAndSay(n-1)

      result = ""
      count = 1
      value = recur[0]
      
      for i in range(1, len(recur)):
        # 연속된 문자가 나오면 count 1씩 증가
        if recur[i] == value:
          count += 1
        # 아닌 경우 result 문자열에 추가
        else:
          result += str(count)
          result += value
          value = recur[i]
          count = 1
  
      result += str(count)
      result += value

      return result



