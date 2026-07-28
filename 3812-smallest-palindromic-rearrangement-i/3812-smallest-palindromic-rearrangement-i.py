class Solution:
    def smallestPalindrome(self, s: str) -> str:
        partision = len(s)//2

        half = ''.join(sorted(s[:partision]))
        
        if len(s) % 2 == 0:
            return half+half[::-1]
        else:
            return half+s[partision]+half[::-1]
            
