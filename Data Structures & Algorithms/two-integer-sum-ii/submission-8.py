class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # iterate through left and right two pointers 
        # -1 -1 1 2 5    target = 3 
        #     l r 
        # sum  
        # target 3 
        
        if len(numbers) == 2:
            return [1, 2]

        map = {}

        for i in range(len(numbers)):
            curr = numbers[i]
            if target-curr in map:
                return [map[target - curr]+1, i+1]
            else:
                map[curr] = i 




