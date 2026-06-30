# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        count = 0
        while fast and count < n:
            fast = fast.next
            count += 1
        
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        if not prev:
            prev = head
            head = None
            head = prev.next
        else:
            prev.next = prev.next.next

        return head
