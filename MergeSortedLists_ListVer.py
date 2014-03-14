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
        avail_list = range(len(lists)) #lists to be extracted
        pri_heap = []
        for i in avail_list:
            if lists[i]:
                heapq.heappush(pri_heap, (lists[i].pop(0),i))
            else:
                avail_list.remove(i)
        while (avail_list or pri_heap):
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
                heapq.heappush(pri_heap, (lists[next_pop].pop(0),next_pop))
                #print str(next_pop)+" pop"
                if not lists[next_pop]:
                    #print "removing"+str(next_pop)
                    avail_list.remove(next_pop)
            else:
                pass
        return phead
                
lists = [[1,5,8],[2,4,8,9],[3,6,9]]
sol = Solution()
head = sol.mergeKLists(lists)
while head.next!=None:
    print head.val
    head=head.next