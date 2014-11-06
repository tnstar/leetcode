# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmHelper(self,left,right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val != right.val:
            return False
        else:
            return (self.isSymmHelper(left.left, right.right) and self.isSymmHelper(left.right, right.left))
    def isSymmetric(self, root):
        if not root:
            return True
        else:
            return self.isSymmHelper(root.left,root.right)