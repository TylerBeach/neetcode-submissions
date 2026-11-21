class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i in range(len(nums)):
            num_needed = target - nums[i]
            
            if num_needed not in map:
                map[nums[i]] = i
            elif num_needed + nums[i] == target:
                return [map[num_needed], i]
        return False
            