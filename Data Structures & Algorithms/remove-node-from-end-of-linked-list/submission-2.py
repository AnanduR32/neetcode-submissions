# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pos = 0

        slow = head
        fast = head

        while fast and pos < n:
            fast = fast.next
            pos += 1
        
        prev = None
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if prev:
            prev.next = slow.next
        else:
            head = head.next
        return head
            
        
