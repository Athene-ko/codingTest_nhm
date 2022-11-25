class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      # EX 1.
      '''
      Input: nums = [5,7,7,8,8,10], target = 8
      Output: [3,4]
      '''

      def left_search(nums: List[int], target: int):
        left, right = 0, len(nums) - 1
        
        while left <= right:
          mid = (left + right) // 2
          if nums[mid] < target:
            left = mid + 1
          else:
            right = mid - 1
        return left
      
      def right_search(nums: List[int], target: int):
        left, right = 0, len(nums) - 1
        
        while left <= right:
          mid = (left + right) // 2
          if nums[mid] <= target:
            left = mid + 1
          else:
            right = mid - 1
        return right

      first = left_search(nums, target)
      last = right_search(nums, target)

      if first <= last:
        return [first, last]

      return [-1, -1]
      