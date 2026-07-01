class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # maxCount = 0
        # count = 0
        # for x in nums:
        #     if x == 1:
        #         count +=1
        #         maxCount = max(count, maxCount)
        #     else:
        #         count = 0
        # return maxCount

        left = 0
        maxLength = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                left = i+1
                
            maxLength = max(i - left+1, maxLength)
        return maxLength
        