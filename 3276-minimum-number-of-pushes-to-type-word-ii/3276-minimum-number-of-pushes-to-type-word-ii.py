class Solution:
    def minimumPushes(self, s: str) -> int:
        return sum(map(mul,sorted(Counter(s).values())[::-1],sorted([1,2,3,4]*8)))
        