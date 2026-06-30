# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    curr: ListNode = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return self.curr
        temp = head.next
        head.next = self.curr
        self.curr = head
        return self.reverseList(temp)
