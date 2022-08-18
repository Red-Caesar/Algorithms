# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# head = ListNode(1, None)
cur_link = head
double_link = head.next
# print(double_link.next.val)
while double_link is not None:
    cur_link = cur_link.next
    if double_link.next is not None:
        double_link = double_link.next.next
    else:
        break

print(cur_link.val)