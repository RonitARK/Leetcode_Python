class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit_sum = 0
            num = nums[i]
            
            while num > 0:
                digit_sum += num % 10
                num = num // 10

            if i == digit_sum:
                return i
                
        return -1