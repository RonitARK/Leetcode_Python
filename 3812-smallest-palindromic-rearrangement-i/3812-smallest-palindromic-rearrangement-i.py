class Solution:
    def smallestPalindrome(self, s: str) -> str:
        partision = len(s)//2

        left = ''.join(sorted(s[:partision]))
        right = left [::-1]
        
        if len(s) % 2 == 0:
            return left+right
        else:
            return left+s[partision]+right
            
