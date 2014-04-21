'''
Created on Mar 17, 2014

@author: C_TLU
'''



#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def __init__(self):
        self.phead = None
    def insert_node_tail (self,pcur,pnext):
        pcur.next = pnext
        pnext.next = None
    def insert_node_2 (self,pprev,pcur):
        ppnext = pprev.next
        pprev.next = pcur
        pcur.next = ppnext
    def find_node_pos(self,phead,pnode):
        pcur = phead
        while pcur:
            pnext = pcur.next
            if pnext == None:
                break
            
            if pcur == phead:
                if pnode.val <= pcur.val:
                    #this means should append before the phead
                    pcur.next = phead
                    phead = pcur
                    self.phead = phead
            else:
                if pnode.val<= pnext.val and pnode.val >=pcur.val:
                    self.insert_node_2(pcur, pnext)
                    break
            pcur = pcur.next
    def insertionSortList(self, head):
        self.phead = head
        phead = head
        pmax = head # pmax means the maxium position in the assertion array
        pcur = head # pcur is the dynamic pointer for the insertion point
        pnext = pcur.next # pnext means next testing node
        
        while pnext:
            if pnext.val > pmax.val:
                pcur = pmax # moving pointer to pmax
                pcur.next = pnext # set next node to pmax.next
                pnext = pnext.next
                if pnext:
                    pnext.next = None
            else:
                temp = pnext.next
                self.find_node_pos(phead,pnext)
                phead = self.phead
                pnext = temp
        return phead
h1 = ListNode(4)
h1.next = ListNode(3)
h1.next.next = ListNode(6)
h1.next.next.next = ListNode(5)
sol = Solution()
test = sol.insertionSortList(h1)
raw_input()