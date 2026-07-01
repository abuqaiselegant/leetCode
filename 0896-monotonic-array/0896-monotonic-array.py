class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i = 1
        if len(nums)==1:
            return True
        if nums[0]<=nums[len(nums)-1]:
            while i < len(nums):
                if nums[i]<nums[i-1]:
                    return False
                i+=1

        else:
            while i < len(nums):
                if nums[i]>nums[i-1]:
                    return False
                i+=1
        return True