#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def getmid(self,phead):
        if not phead:
            return None
        if not phead.next:
            return phead
        pslow = phead
        pfast = phead.next
        while pfast and pfast.next:
            pslow = pslow.next
            pfast = pfast.next
            pfast = pfast.next
        return pslow
    def merge(self,heada,headb):
        if not heada:
            return headb
        if not headb:
            return heada
        pcur = ListNode(-1)
        phead = pcur
        while heada and headb:
            if heada.val<headb.val:
                pcur.next = heada
                pcur = pcur.next
                heada = heada.next
            else:
                pcur.next = headb
                pcur = pcur.next
                headb = headb.next
        if heada:
            pcur.next = heada
        if headb:
            pcur.next = headb
        return phead.next
    def sort(self,phead):
        if not phead or not phead.next:
            return phead
        mid = self.getmid(phead)
        if mid:
            pnext = mid.next
            mid.next = None
        return self.merge(self.sort(phead),self.sort(pnext))
    def printll(self,phead):
        while phead:
            print phead.val,
            phead=phead.next
sol = Solution()
pcur = ListNode(5)
phead = pcur
pcur.next = ListNode(4)
pcur = pcur.next
pcur.next = ListNode(3)
pcur = pcur.next
pcur.next = ListNode(2)
pcur = pcur.next
pcur.next = ListNode(1)
ptemp = sol.sort(phead)
print sol.printll(ptemp)