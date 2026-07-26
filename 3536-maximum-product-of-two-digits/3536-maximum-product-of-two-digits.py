class Solution:
    def maxProduct(self, n: int) -> int:
        num = list((str(n)))
        num.sort(reverse = True)
        return int(num[0]) * int(num[1])
        