class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for idx in range(len(nums)):
        #     for check in range(idx + 1, len(nums)):
                
        #         if nums[idx] + nums[check] == target:
        #             return [idx, check]
        # return []

        dic = {}
        n = len(nums)

        for idx in range(n):
            otherNumber = target - nums[idx]
            if otherNumber in dic:
                return [dic[otherNumber], idx]
            dic[nums[idx]] = idx
        return []
            
        