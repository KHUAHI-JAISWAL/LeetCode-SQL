# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:

        # Brute Force: Nodes ko list mein store karke odd/even positions arrange karo.
        # O(n) time, O(n) space.

        # Best (Two Pointer): Odd aur even positions ke links ko directly rearrange karo.
        # O(n) time, O(1) space.

        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head
        