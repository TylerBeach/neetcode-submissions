class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1

        record = 0

        while left < right:
            shortest = min(heights[left], heights[right])
            width = right - left
            amount = shortest * width
            record = max(amount, record)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return record