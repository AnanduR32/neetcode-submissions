class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 1
        maxValue = 0
        area = 0
        size = len(height)
        leftBoundary = [0] * size
        rightBoundary = [0] * size 
        for (idx, value) in enumerate(height):
            leftBoundary[idx] = max(value, leftBoundary[idx - 1])
        for (idx, value) in enumerate(reversed(height)):
            rightBoundary[idx] = max(value, rightBoundary[idx - 1])
        rightBoundary.reverse()
        for i in range(1, size):
            length = min(leftBoundary[i], rightBoundary[i])
            area += max(0, length - height[i])

        return area

        