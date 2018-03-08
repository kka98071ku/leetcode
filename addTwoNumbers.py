# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode

    Pitfall: it's easy to forget the `plusONe != 0` check
    """
    head = ListNode(0)
    current, plusOne = head, 0
    while l1 != None or l2 != None or plusOne != 0:
        summation = plusOne + (0 if l1 == None else l1.val) + \
            (0 if l2 == None else l2.val)
        plusOne = 1 if summation > 9 else 0
        current.next = ListNode(summation % 10)
        current = current.next
        if l1 != None:
            l1 = l1.next
        if l2 != None:
            l2 = l2.next
    return head.next
