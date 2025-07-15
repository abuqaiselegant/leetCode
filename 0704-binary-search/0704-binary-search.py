class Solution(object):
    # def search(self, nums, target):
        # """
        # :type nums: List[int]
        # :type target: int
        # :rtype: int
        # """
        # start = 0
        # end = len(nums)-1
        # while start<=end:
        #     mid = start+(end-start)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid]>target:
        #         end=mid-1
        #     else:
        #         start = mid+1
        # return -1
    def search(self, nums, target):
        return self.binarySearch(0, len(nums)-1,nums, target)

    def binarySearch(self, start, end, nums, target):
        if start>end:
            return -1
        mid = start+(end-start)//2
        if nums[mid]==target:
            return mid
        if nums[mid]>target:
            return self.binarySearch(start, mid-1,nums,target)
        return self.binarySearch(mid+1, end, nums, target)
    
    