#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        pseudo_head = ListNode(-1)
        pseudo_head.next = head
        ptr_slow = pseudo_head
        ptr_slow_prev = pseudo_head
        ptr_fast = pseudo_head
        for i in range(n):
            ptr_fast = ptr_fast.next
        while ptr_fast !=None:
            ptr_fast = ptr_fast.next
            ptr_slow_prev = ptr_slow
            ptr_slow = ptr_slow.next
        # we found it need to check if it is the first node/last_node
        ptr_slow_prev.next = ptr_slow.next
        del ptr_slow
        return pseudo_head.next
    
phead = ListNode(1);
phead.next = ListNode(2);
sol = Solution();
phead = sol.removeNthFromEnd(phead, 1)
print phead
       