# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def detectCycle(self, head):
        templist = []
        while head != None:
            if head not in templist:
                templist.append(head)
                head = head.next
            else:
                return head
        return None