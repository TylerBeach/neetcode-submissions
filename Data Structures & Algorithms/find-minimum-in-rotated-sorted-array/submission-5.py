class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        the_min = float("inf")
        
        
        while l < r:
            m = l + (r - l) // 2
            the_min = min(the_min, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1 



        return min(the_min, nums[l])




# l = 3 
# r = 2 
# m = 0 + 6 / 2 = 3 -> 6

# # 3,4,5,6,1,2
# if l < m and l > r 
#     m = r

# # 4,5,6,1,2,3
# elif l > m and l > r
#     m = r 

# elif l < m and l < r 

# # 1 2 3 4 5 6  