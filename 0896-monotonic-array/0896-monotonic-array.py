class Solution:
    # def isMonotonic(self, nums: List[int]) -> bool:
    #     i = 1
    #     if len(nums)==1:
    #         return True
    #     if nums[0]<=nums[len(nums)-1]:
    #         while i < len(nums):
    #             if nums[i]<nums[i-1]:
    #                 return False
    #             i+=1

    #     else:
    #         while i < len(nums):
    #             if nums[i]>nums[i-1]:
    #                 return False
    #             i+=1
    #     return True
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            elif nums[i] < nums[i - 1]:
                increasing = False

        return increasing or decreasing