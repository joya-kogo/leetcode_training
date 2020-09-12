# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        now = head
        prev_dict = {}
        length = 0
        prev = None
        while True:
            prev_dict[length] = prev
            length += 1
            prev = now
            now = now.next
            if now == None:
                break
        if n == length:
            return head.next
        elif n == 1:
            prev_dict[length - 1].next = None
            return head
        else:
            prev_dict[length - n].next = prev_dict[length - n].next.next
            return head
            
        