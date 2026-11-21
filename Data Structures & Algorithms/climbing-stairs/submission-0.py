class Solution:
    def climbStairs(self, n: int) -> int:

        left, right = 1, 1

        for i in range(0, n - 1):
            
            new_val = left + right
            right = left 
            left = new_val

        return left