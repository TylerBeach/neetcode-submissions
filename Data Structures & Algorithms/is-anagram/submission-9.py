class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_one, map_two = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):

            if s[i] not in map_one:
                map_one[s[i]] = 1
            else:
                map_one[s[i]] += 1

            if t[i] not in map_two:
                map_two[t[i]] = 1
            else:
                map_two[t[i]] += 1

        return map_one == map_two