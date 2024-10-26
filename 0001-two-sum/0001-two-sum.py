class Solution:
    def twoSum(self, nums, target) :
        a={}
        for count,ele in enumerate(nums):
            contemperory= target-ele
            if contemperory in a:
                return [a[contemperory],count]
            a[ele]=count
        return []