# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        old_node = None
        node_list = []
        up_flag = 0
        while True:
            raw_v = l1.val + l2.val + up_flag
            up_flag = raw_v//10
            v = raw_v%10
            new_node = ListNode(v)
            node_list.append(new_node)
            if l1.next ==None and l2.next == None:
                if up_flag != 0:
                    node_list.append(ListNode(up_flag))
                break
            if l1.next == None:
                l1 = ListNode(0)
            else:
                l1 = l1.next
            if l2.next == None:
                l2 = ListNode(0)
            else:
                l2 = l2.next
        for i in range(len(node_list)-1):
            node_list[i].next = node_list[i+1]
        return node_list[0]
        