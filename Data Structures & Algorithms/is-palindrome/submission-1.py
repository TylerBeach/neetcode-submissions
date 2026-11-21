class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # list_s = [char.lower() for char in s if char.isalpha()]
        list_s = []
        for char in s:
            if char.isalpha() or char.isnumeric():
                list_s.append(char.lower())

        l, r = 0, len(list_s)-1
        while l <= r:
            if list_s[l] != list_s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True