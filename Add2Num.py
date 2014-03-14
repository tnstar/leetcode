'''
Created on Mar 14, 2014

@author: C_TLU
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# 342+465=807
# 2 + 5 = 7
# 6 + 4 = 0 Carrier:1
# 2 + 5 + 1 = 8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        Carrier = 0
        answer = None
        pcur = None
        while l1 or l2 or Carrier:
            print Carrier,"Carry"
            sum2 = 0
            if l1 != None:
                sum2 = sum2 + l1.val
                l1 = l1.next
            if l2 != None:
                sum2 = sum2 + l2.val
                l2 = l2.next
            sum2 = sum2 + Carrier
            if sum2 > 9 :
                sum2 = sum2%10
                Carrier = 1
            else:
                Carrier = 0
            if answer == None:
                answer = ListNode(sum2)
                pcur=answer
            else:
                pcur.next = ListNode(sum2)
                pcur = pcur.next
        return answer
h1 = ListNode(1)
h2 = ListNode(9)
h2.next = ListNode(9)                
lists = [h1,h2]
sol = Solution()
head = sol.addTwoNumbers(h1,h2)
print head
while head!=None:
    print head.val
    head=head.next