# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:


        #Brute Force: Har node ke liye uske twin node ko traverse karke sum nikalo → O(n²) Time, O(1) Space.
        #Best Approach: Slow-fast pointers se middle find karo, second half reverse karke corresponding nodes ka sum calculate karo → O(n) Time, O(1) Space.


        # Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Calculate maximum twin sum
        first = head
        second = prev
        max_sum = 0

        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
        