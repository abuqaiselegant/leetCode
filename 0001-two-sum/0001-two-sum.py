class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDic = {}
        for i in range(len(nums)):
            if target - nums[i] not in  numsDic:
                numsDic[nums[i]] = i
            else:
                return [numsDic[target-nums[i]], i]        