class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # l=0
        # min_len = float('inf')
        # total = 0
        # for r in range(len(nums)):
        #     total +=nums[r]
        #     while total >=target:
        #         min_len =min(min_len,r-l+1)
        #         total-=nums[l]
        #         l+=1
        # return 0 if min_len ==float('inf') else min_len

        l = 0
        r = 0
        minlen = float('inf')
        currSum = 0
        while r <len(nums):
            currSum += nums[r]
            while currSum>=target:
                minlen =min(minlen,r-l+1)
                currSum-=nums[l]
                l+=1
            r+=1
        return 0 if minlen ==float('inf') else minlen