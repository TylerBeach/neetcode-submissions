class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sol = []

        # 9 9 9 
        # 1 2 3 4
        added = False 
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9 and not added:
                sol.append(digits[i]+1)
                added = True
            else:
                # we have to carry it over
                if added:
                    sol.append(digits[i])
                else:
                    sol.append(0)
                

        if not added:
            sol.append(1)        
        sol = sol[::-1]

        return sol