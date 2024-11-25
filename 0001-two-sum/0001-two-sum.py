class Solution:
    def twoSum(self, nums, target) :
        """a={}
        for count,ele in enumerate(nums):
            contemperory= target-ele
            if contemperory in a:
                return [a[contemperory],count]
            a[ele]=count
        return []"""
        hash = {}
        for i in range(len(nums)):
            com = target -nums[i]
            if com in hash:
                return [i,hash[com]]
            else:
                hash[nums[i]]=i
        return []
    
    