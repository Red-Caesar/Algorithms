# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# head = ListNode(1, (ListNode(2, ListNode(3, None))))
# cur = head.next
# while cur.next is not None:
#     cur = cur.next
# cur.next = head.next

# 1st solution
# if head is not None:
#     node_dict = dict()
#     cur = head
#     while cur.next is not None:
#         if cur not in node_dict:
#             node_dict[cur] = True
#         else:
#             print(cur.val)
#             break
#         cur = cur.next
# print(None)

# 2nd solution
class Solution:
    def detectCycle(self, head):
        if head is None: return(None)
        cur = head
        double = head
        while double is not None:
            cur = cur.next
            if double.next and double.next.next is not None:
                double = double.next.next
            else:
                return(None)
            if double == cur:
                break
        double = head
        while double != cur:
            double = double.next
            cur = cur.next
        return(cur)

