# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        fast:ListNode = head
        slow:ListNode = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        count = 0
        curr = head
        while prev:
            first_next = curr.next
            second_next = prev.next
            curr.next = prev
            prev.next = first_next
            prev = second_next
            curr = first_next
            
        