class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)

        boundLeft = [0] * size
        boundRight = [0] * size

        prev = 0
        for idx in range(1, size):
            if height[idx - 1] > height[idx]:
                boundLeft[idx] = max(height[idx - 1], boundLeft[idx - 1])
            else:
                boundLeft[idx] = boundLeft[idx - 1]
        for idx in range(size - 2, -1, -1):
            if height[idx + 1] > height[idx]:
                boundRight[idx] = max(height[idx + 1], boundRight[idx + 1])
            else:
                boundRight[idx] = boundRight[idx + 1]

        fill = 0
        for idx in range(size):
            fill += max(min(boundLeft[idx], boundRight[idx]) - height[idx],0)

        return fill
            