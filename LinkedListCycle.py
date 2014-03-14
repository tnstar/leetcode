'''
Created on Mar 14, 2014

@author: C_TLU
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        head1 = head
        head2 = head
        while True:
            if head1 == None:
                return False
            head1=head1.next
            if head2 == None:
                return False
            head2 = head2.next
            if head2 == None:
                return False
            head2 = head2.next
            if head1 == head2:
                return True