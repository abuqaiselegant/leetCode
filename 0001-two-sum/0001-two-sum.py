class Solution:

    
    def twoSum(self, nums, target):
        a = {}
        for i in range(len(nums)):
            com = target - nums[i]
            if com in a:
                return[i, a[com]]
            else:
                a[nums[i]]=i
        return []