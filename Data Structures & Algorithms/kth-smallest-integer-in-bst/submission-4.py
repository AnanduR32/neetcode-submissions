# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    heap = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []
        if root is None:
            return None
        self.constructHeap(root)
        for i in range(1, k):
            heapq.heappop(self.heap)
        return self.heap[0]

    def constructHeap(self, root: TreeNode):
        if root:
            heapq.heappush(self.heap, root.val)
        if root and root.left:
            self.constructHeap(root.left)
        if root and root.right:
            self.constructHeap(root.right)
        