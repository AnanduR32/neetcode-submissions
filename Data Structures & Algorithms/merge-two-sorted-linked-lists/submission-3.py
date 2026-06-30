# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        head3 = ListNode()
        back3 = head3
        while head1 and head2:
            if head1.val < head2.val:
                head3.next = head1
                head1 = head1.next
            else:
                head3.next = head2
                head2 = head2.next
            head3 = head3.next
        while head1:
            head3.next = head1
            head1, head3 = head1.next, head3.next
        while head2:
            head3.next = head2
            head2, head3 = head2.next, head3.next
        back3 = back3.next
        return back3
