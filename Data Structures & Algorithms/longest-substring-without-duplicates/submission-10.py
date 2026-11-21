class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0 
        answer_set = set()

        for r in range(len(s)):
            while s[r] in answer_set:
                answer_set.remove(s[l])
                l += 1
            answer_set.add(s[r])
            longest = max(longest, len(answer_set))    

        return longest