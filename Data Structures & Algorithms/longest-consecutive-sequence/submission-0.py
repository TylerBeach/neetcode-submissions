class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numsSet = set(nums)
        longest = 0

        for number in nums:
            if (number - 1) not in numsSet:
                length = 0
                while (number + length) in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest