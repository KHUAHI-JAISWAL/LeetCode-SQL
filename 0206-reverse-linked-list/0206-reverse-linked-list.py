# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:


        #Brute Force: Nodes ko list/array mein store karke reverse order mein new linked list banao → O(n) Time, O(n) Space.
        #Best Approach: prev, curr pointers se links ko in-place reverse karo → O(n) Time, O(1) Space


        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
        