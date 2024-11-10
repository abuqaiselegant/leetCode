class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        if nums[0]<=nums[len(nums)-1]:
            for i in range(len(nums)-1):
                if nums[i+1]<nums[i]:
                    return False
        else:
            for i in range(len(nums)-1):
                if nums[i+1]>nums[i]:
                    return False
        return True"""
        inc = dec = True
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                inc = False
            if nums[i+1]>nums[i]:
                dec = False
            if inc ==False and dec == False:
                return False
        return True
            
        