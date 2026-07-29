class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        original = x
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        while x != 0:
            rem = int(x % 10)
            num = (num*10) + rem
            x = x // 10
        return original == num   

        