class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1


        while l < r:
            m = r - l
            if target == nums[m]:
                return m

            if target > nums[m]:
                l = m + 1 
            elif target < nums[m]:
                r = m - 1  

        if nums[0] == target:
            return 0
        return -1