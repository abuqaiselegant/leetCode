class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize-1
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum+=nums[j]
                maxi = max(maxi, sum)
        return maxi
            