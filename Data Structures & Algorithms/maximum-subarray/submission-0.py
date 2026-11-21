class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # [2,-3,4,-2,2,1,-1,4]

        curr_sum = 0
        highest_sum = nums[0]


        for num in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num

            highest_sum = max(highest_sum, curr_sum)

        return highest_sum