class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while not s[left].isalnum() and left < right:
                left+=1
            while not s[right].isalnum() and left < right:
                right-=1

            if left >= right:
                return True

            left_char = s[left].lower()
            right_char = s[right].lower()

            if left_char == right_char:
                left+=1
                right-=1
            else:
                return False

        return True