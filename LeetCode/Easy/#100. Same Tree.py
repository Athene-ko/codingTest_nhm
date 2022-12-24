# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # val, left, right is None => False
        # val, left, right 모두 같음 => True

        ## 둘다 None 인 경우
        if not p and not q:
            return True
    
        # 둘 중 하나만 None 인 경우
        elif not p or not q:
            return False

        # 재귀 활용
        else:
            if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True