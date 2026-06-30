class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while (left < right):
            length = right - left
            height = min(heights[left], heights[right])
            maxArea = max(maxArea, height*length)
            if (heights[left] > heights[right]):
                right -= 1
            else:
                left += 1
        return maxArea