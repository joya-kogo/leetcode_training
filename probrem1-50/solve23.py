# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        count = 0
        before_even = None
        before_odd = head
        now = head
        while now != None:
            temp = now.next
            if count % 2 == 1:
                if before_even != None:
                    before_even.next = now
                else:
                    head = now
                now.next = before_odd
                before_odd.next = temp
                before_even = now.next
            else:
                before_odd = now
            now = temp
            count += 1
        return head