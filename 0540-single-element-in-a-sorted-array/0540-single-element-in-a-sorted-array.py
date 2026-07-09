class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # i = 0
        # while i <len(nums)-1:
        #     if nums[i]!=nums[i+1]:
        #         return nums[i]
        #     i+=2
        # return nums[i]
        
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if mid%2 ==1:
                mid = mid-1
            if nums[mid]!=nums[mid+1]:
                right = mid
            else:
                left = mid+2
        return nums[left]