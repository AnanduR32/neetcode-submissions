# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next 
        slow.next = None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        curr = head
        while prev:
            print(curr.val)
            next_curr = curr.next
            next_revr = prev.next
            prev.next = next_curr
            curr.next = prev 
            curr = next_curr
            prev = next_revr


        