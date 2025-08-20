class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]
        # for i in range(len(nums)):
        #     count =1
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             count+=1
        #         if count > len(nums)/2:
        #             return nums[i]
        # return -1
        x,count =None,0
        for num in nums:
            if count == 0:
                x = num
            if x == num:
                count+=1
            else :
                count-=1
        return x
