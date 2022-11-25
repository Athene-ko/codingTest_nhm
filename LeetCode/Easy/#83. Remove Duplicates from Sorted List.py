# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy 노드 생성
        dummy = head

        while dummy.next:
            # val == next.val 이면, next.next와 연결
            if dummy.next and dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            # 아닌 경우, 그대로
            else:
                dummy = dummy.next
        
        return head