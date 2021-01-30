class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # recursion version
        new_head = ListNode(None)
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            new_head.next = l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        else:
            new_head.next = l2
            l2.next = self.mergeTwoLists(l2.next, l1)
        return new_head.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        new_head = ListNode(0)
        curr_new = new_head
        while curr1 and curr2:
            val1 = curr1.val
            val2 = curr2.val
            if val1 < val2:
                curr_new.next = ListNode(val1)
                curr1 = curr1.next
            else:
                curr_new.next = ListNode(val2)
                curr2 = curr2.next
            curr_new = curr_new.next
        if curr1:
            curr_new.next = curr1
        elif curr2:
            curr_new.next = curr2
        else:
            pass
        return new_head.next