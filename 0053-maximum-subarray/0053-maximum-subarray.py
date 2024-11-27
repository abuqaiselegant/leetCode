class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize-1
        sum =0
        for i in range(len(nums)):
            sum+=nums[i]
            maxi = max(sum, maxi)
            if sum<0:
                sum =0
        return maxi
            