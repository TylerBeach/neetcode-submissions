class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        for i, a in enumerate(nums):
            # logic is that this is our first number so if
            # its bigger than 0 the numbers to the right
            # are also bigger than zero so we > 0 always
            if a > 0:
                break

            # logic is that we are at second last therefore nothing
            # else to add since we need 3 nums
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                # if its bigger than we move the right to the left so we can hopefully
                # get a smaller number lowering the sum 
                if threeSum > 0:
                    r -= 1
                # if its smaller we walk left to the right to try and increase the sum
                elif threeSum < 0:
                    l += 1
                else:
                    sol.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # keep walking so that we can 
                    # try to find other remaining solutions since we could have
                    # a=-4 l=-2 r=6 then have a=-4 l=-1 r=5
                    # -4, -2, -1, 5, 6 as an example

                    # here we are just walking the left to the right til its not the same 
                    # since duplicates are not allowed
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return sol