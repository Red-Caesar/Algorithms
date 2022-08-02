class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
arr = []
while head:
    arr.append(head.val)
    head = head.next
arr.reverse()
new_head = ListNode()
list1 = new_head
for i, el in enumerate(arr):
    list1.val = el
    if i != len(arr)-1:
        list1.next = ListNode()
        list1 = list1.next
print(arr)