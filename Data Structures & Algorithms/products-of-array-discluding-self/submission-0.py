class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [1] * (len(nums))

        # this will iterate through them once adding the preFix amount to each value
        # [1, 2, 4, 6] -> [1, 1*1, 1*1*2, 1*1*2*4] => [1, 1, 2, 8]
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        
        # now we can go backwards and multiply the array with the POSTfix to each value
        # [1, 1, 2, 8] ->  [1*6*4*2, 1*6*4, 2*6, 8*1] => [48, 24, 12, 8]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans 