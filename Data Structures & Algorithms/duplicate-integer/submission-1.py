class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer_set = set(nums)
        return len(answer_set) != len(nums) 