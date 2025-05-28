# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
          return head

        odd_head = head
        even_head = head.next
        even = even_head

        while even and even.next:
            odd_head.next = even.next
            odd_head = odd_head.next
            even.next = odd_head.next
            even = even.next

        odd_head.next = even_head
        return head