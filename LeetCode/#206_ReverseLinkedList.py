from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            new_head = ListNode()
            arr.reverse()
            list1 = new_head
            for i, el in enumerate(arr):
                list1.val = el
                if i != len(arr)-1:
                    list1.next = ListNode()
                    list1 = list1.next
            return new_head
        else:
            return head
    def secondSolution(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        def helper(node):
            if node.next is None:
                return node
            ans = helper(node.next)
            node.next.next = node
            return ans

        ans = helper(head)
        head.next = None
        return ans


s = Solution()
print(s.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))))
print(s.reverseList(ListNode(1, ListNode(2, None))))
print(s.reverseList(None))
