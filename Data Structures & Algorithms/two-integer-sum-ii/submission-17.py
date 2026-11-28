class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # iterate through left and right two pointers 
        #  1, 2, 5, 7, 9     target = 12
        #        l     r 
        # curr = 10 
        
        left, right = 0, len(numbers)-1
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left + 1, right + 1]

            if numbers[right] >= target and curr > target:
                right -= 1
            elif curr < target:
                left += 1
            else:
                right -= 1 

        return [left + 1, right + 1]



