class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
      """
      Do not return anything, modify nums1 in-place instead.
      """
      ## 각 리스트의 끝 인덱스부터 역순으로 크기 비교하기

      # m과 n 이 모두 존재하는 경우
      while m > 0 and n > 0:
        # 만약 num1의 값이 nums2의 값보다 크면, nums1의 값으로 대체
        if nums1[m-1] > nums2[n-1]:
          nums1[m+n-1] = nums1[m-1]
          m -= 1
        # 만약 num2의 값이 nums1의 값보다 크면, nums2의 값으로 대체
        else:
          nums1[m+n-1] = nums2[n-1]
          n -= 1
      # m = 0 이고 n 만 존재하는 경우, nums1을 nums2으로 대체
      while n > 0:
        nums1[n-1] = nums2[n-1]
        n -= 1

