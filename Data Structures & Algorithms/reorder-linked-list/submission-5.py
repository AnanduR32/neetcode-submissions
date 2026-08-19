# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        rev = slow.next
        slow.next = None
        prev = None
        while rev:
            rev.next, prev, rev = prev, rev, rev.next

        curr = head
        while prev:
            currNext = curr.next
            prevNext = prev.next
            curr.next = prev
            prev.next = currNext
            prev = prevNext
            curr = currNext
        

        
