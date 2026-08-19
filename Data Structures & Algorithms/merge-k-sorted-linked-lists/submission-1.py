# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []

        for idx,node in enumerate(lists):
            while node:
                heapq.heappush(q, node.val)
                node = node.next
        
        head = ListNode()
        node = head
        while q:
            node.next = ListNode(heapq.heappop(q))
            node = node.next
        
        return head.next

