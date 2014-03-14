'''
@author: TNSTAR
'''
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        head = None
        phead = None
        next_pop = -1
        pri_heap = []
        avail_list = range(len(lists))
        for i in avail_list:
            if lists[i]:
                heapq.heappush(pri_heap, (lists[i].val,i))
                lists[i] = lists[i].next
        while pri_heap:
            if head == None:
                temp = heapq.heappop(pri_heap)
                #print temp[0]
                head = ListNode(temp[0])
                phead = head
                next_pop = temp[1]
                #print str(next_pop)+" next"
            else:
                temp = heapq.heappop(pri_heap)
                #print temp[0]
                head.next = ListNode(temp[0])
                head = head.next
                next_pop = temp[1]
                #print str(next_pop)+" next"
            if lists[next_pop]:
                heapq.heappush(pri_heap, (lists[next_pop].val,next_pop))
                lists[next_pop] = lists[next_pop].next
                #print str(next_pop)+" pop"
            else:
                pass
        return phead

h1 = ListNode(1)
h1.next = ListNode(3)
h2 = ListNode(2)
h2.next = ListNode(4)                
lists = [h1,h2]
sol = Solution()
head = sol.mergeKLists(lists)
while head!=None:
    print head.val
    head=head.next