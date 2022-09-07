from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer_first = None
        pointer_second = head
        while pointer_second is not None:
            pointer_second = pointer_second.next
            n -= 1
            if n < 0:
                if pointer_first is None:
                    pointer_first = head
                else:
                    pointer_first = pointer_first.next
        if pointer_first is None:
            return head.next
        elif pointer_first.next is not None:
            pointer_first.next = pointer_first.next.next
            return head


s = Solution
print(s.removeNthFromEnd(s, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 2))
print(s.removeNthFromEnd(s, ListNode(1, None), 1))
print(s.removeNthFromEnd(s, ListNode(1, ListNode(2, None)), 1))
