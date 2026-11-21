class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ans_dict = {}
        freq = [[] for i in range(len(nums) + 1)]



        for num in nums:
            if num in ans_dict:
                ans_dict[num] += 1
            else:
                ans_dict[num] = 1
        
        for key, value in ans_dict.items():
            freq[value].append(key)

        answer = []
        for i in range(len(freq) - 1, 0, -1):
            for number in freq[i]:
                answer.append(number)
                if len(answer) == k:
                    return answer
                

        return answer