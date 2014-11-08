#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        phead = ListNode(-2147483648)
        phead.next = head
        psorted = head
        while psorted.next:
            print "iteration"
            psearch = head
            pprev = phead
            while True:
                print psearch.val,psorted.val
                if psearch == psorted:
                    if psorted.next.val<psearch.val:
                        temp_node = psorted.next
                        pprev.next = temp_node
                        psorted.next = psearch.next.next
                        temp_node.next = psorted
                    else:
                        psorted = psorted.next
                    break
                else:
                    if psearch.val>psorted.next.val:
                        temp_node = psorted.next
                        pprev.next = temp_node
                        psorted.next = psorted.next.next
                        temp_node.next = psearch
                    else:
                        psearch = psearch.next
                        pprev = pprev.next
        return phead.next

phead = ListNode(3)
phead.next = ListNode(2)
phead.next.next = ListNode(1)

sol = Solution()

ph = sol.insertionSortList(phead)
while ph:
    print ph.val