class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ans_dict = {}

        for num in nums:
            if num in ans_dict:
                ans_dict[num] += 1
            else:
                ans_dict[num] = 1
        
        # sorted(ans_dict, key=ans_dict.get)
        ans_dict = sorted(ans_dict.items(), key=lambda kv: kv[1], reverse=True)
        print(ans_dict)
        answer = []
        for i in range(k):
            answer.append(ans_dict[i][0])

        return answer