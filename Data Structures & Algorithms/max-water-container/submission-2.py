class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        total = 0

        while left < right:
            width = left - right 
            width = abs(width)
            height = min(heights[left], heights[right])
            current_w = width * height
            total = max(total, current_w)

            if heights[left] > heights[right] or heights[left] == heights[right]:
                right -= 1
            else:
                left += 1
        
        return total