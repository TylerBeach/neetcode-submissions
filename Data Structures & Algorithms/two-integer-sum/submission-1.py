class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment not in nums_map:
                nums_map[nums[i]] = i
            else:
                return [nums_map[compliment], i]

        return False