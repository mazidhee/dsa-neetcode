class Solution:
    def isPalindrome(self, s: str) -> bool:
        nl = [char.lower() for char in s if char.isalnum()]
        al = "".join(nl)
        left = 0
        right = len(al) - 1

        while left < right:
            if al[left] == al[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

        
        
