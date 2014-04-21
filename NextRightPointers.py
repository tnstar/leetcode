'''
Created on Apr 7, 2014

@author: c_tlu
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root.left == None or root == None:
            return
        parent = root
        son = parent.left
        while son:
            #move to next layer
            #store next layer parent node
            node_start = son
            while son:
                son.next = parent.right
                parent = parent.next
                son = son.next
                if parent:
                    son.next = parent.left
                else:
                    son.next = None
                son = son.next
            parent = node_start
            son = parent.left
                
        