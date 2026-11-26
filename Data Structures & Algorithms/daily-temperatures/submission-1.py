class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)   
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                sol[stackIndex] = (index - stackIndex)
            stack.append([temperature, index])
        return sol

        # 30 38 30 36 35 40 28 
        #  1  0  0  0  0  0  0
        # [[38, 1]] 
