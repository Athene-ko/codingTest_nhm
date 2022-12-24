class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = {}  # { num : count } 형태를 위한 dictionary 선언

        for num in nums:
            # dictionary 에서 해당 키 있는지 확인 (없는 경우, 0 반환)
            cnt = answer.get(num, 0)

            # 인덱스 + 1
            answer[num] = cnt + 1
        
        # 개수가 1인 경우 해당하는 키(key) 반환
        for key, value in answer.items():
            if value == 1: 
                return key