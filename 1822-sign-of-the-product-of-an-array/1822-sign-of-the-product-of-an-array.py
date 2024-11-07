def signFunc(x):
        if x>0:
            return 1
        elif x<0:
            return -1
        else:
            return 0
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum =1
        for i in range(len(nums)):
            sum*=nums[i]
        return signFunc(sum)
    def signFunc(x):
        if x>0:
            return 1
        elif x<0:
            return -1
        else:
            return 0
        