class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))
head = ListNode()
next_h = head
next1 = list1
next2 = list2
while next1 or next2:
    if next1 is None:
        next_h.val = next2.val
        next2 = next2.next
    elif next2 is None:
        next_h.val = next1.val
        next1 = next1.next
    elif next1.val > next2.val:
        next_h.val = next2.val
        next2 = next2.next
    else:
        next_h.val = next1.val
        next1 = next1.next
    if next1 is not None or next2 is not None:
        next_h.next = ListNode()
        next_h = next_h.next

print(head)