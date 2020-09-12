# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans_vals = []
        while l1 != None:
            ans_vals.append(l1.val)
            l1 = l1.next
        while l2 != None:
            ans_vals.append(l2.val)
            l2 = l2.next
        ans_vals.sort()
        next_node = None
        now = None
        for v in reversed(ans_vals):
            now = ListNode(v, next_node)
            next_node = now
        return now
            